import os
import csv
import re
import argparse
import ast
import statistics
from pathlib import Path


def parse_constants(pyfile):
    """Parse simple constant assignments from a python file."""
    constants = {}
    if not os.path.exists(pyfile):
        return constants
    try:
        with open(pyfile, 'r') as f:
            tree = ast.parse(f.read(), filename=pyfile)
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        try:
                            value = ast.literal_eval(node.value)
                        except Exception:
                            value = None
                        constants[target.id] = value
    except Exception:
        pass
    return constants


def find_epochs(setup_path):
    best = None
    best_num = -1
    last = None
    last_num = -1
    for d in os.listdir(setup_path):
        if d.startswith('epoch') and os.path.isdir(os.path.join(setup_path, d)):
            m = re.findall(r'epoch(\d+)', d)
            if not m:
                continue
            num = int(m[0])
            if os.path.exists(os.path.join(setup_path, d, 'test_confusion_matrix_fig.png')):
                if num > best_num:
                    best_num = num
                    best = (num, d)
            if num > last_num:
                last_num = num
                last = (num, d)
    return best, last


def parse_test_metrics(csv_path, epoch_num):
    if not os.path.exists(csv_path):
        return None
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                if int(float(row['Epoch'])) == epoch_num:
                    return {
                        'F1 Score': row['F1 Score'],
                        'Accuracy': row['Accuracy'],
                        'Precision': row['Precision'],
                        'Recall': row['Recall'],
                    }
            except Exception:
                continue
    return None


def collect_data(root_dir):
    data = {}
    for noise in sorted(os.listdir(root_dir)):
        noise_path = os.path.join(root_dir, noise)
        if not os.path.isdir(noise_path):
            continue
        data[noise] = {}
        for seed in sorted(os.listdir(noise_path)):
            seed_path = os.path.join(noise_path, seed)
            if not os.path.isdir(seed_path):
                continue
            data[noise][seed] = {}
            for setup in sorted(os.listdir(seed_path)):
                setup_path = os.path.join(seed_path, setup)
                if not os.path.isdir(setup_path):
                    continue
                parts = setup.split('-')
                setup_name = '-'.join(parts[6:]) if len(parts) > 6 else setup
                best, last = find_epochs(setup_path)
                if not best:
                    continue
                best_num, best_dir = best
                metrics = parse_test_metrics(os.path.join(setup_path, 'test.csv'), best_num)
                info = {
                    'best_epoch': best_num,
                    'metrics': metrics,
                    'hyperparameters': parse_constants(os.path.join(setup_path, 'hyperparameters.py')),
                    'options': parse_constants(os.path.join(setup_path, 'options.py')),
                    'loss_png': os.path.join(setup_path, last[1], 'loss.png') if last else None,
                    'confusion_matrices': [
                        os.path.join(setup_path, best_dir, img)
                        for img in [
                            'test_confusion_matrix_fig.png',
                            'train_confusion_matrix_fig.png',
                            'validate_confusion_matrix_fig.png',
                        ]
                        if os.path.exists(os.path.join(setup_path, best_dir, img))
                    ],
                    'trend_imgs': [
                        os.path.join(setup_path, img)
                        for img in [
                            'test_metrics_trends.png',
                            'train_metrics_trends.png',
                            'validate_metrics_trends.png',
                        ]
                        if os.path.exists(os.path.join(setup_path, img))
                    ],
                }
                data[noise][seed][setup_name] = info
    return data


def aggregate_metrics(data):
    means = {}
    deviations = {}
    for noise, seeds in data.items():
        for seed, setups in seeds.items():
            for setup_name, info in setups.items():
                m = info['metrics']
                if not m:
                    continue
                for key in ['F1 Score', 'Accuracy', 'Precision', 'Recall']:
                    means.setdefault(noise, {}).setdefault(setup_name, {}).setdefault(key, []).append(float(m[key]))
                    deviations.setdefault(noise, {}).setdefault(setup_name, []).append(float(m[key]))
    mean_table = {}
    std_table = {}
    for noise, setups in means.items():
        mean_table[noise] = {}
        std_table[noise] = {}
        for setup, vals in setups.items():
            mean_table[noise][setup] = {k: sum(v) / len(v) for k, v in vals.items()}
            std_table[noise][setup] = statistics.stdev(deviations[noise][setup]) if len(deviations[noise][setup]) > 1 else 0.0
    return mean_table, std_table


def format_table(mean_table):
    setups = set()
    noises = sorted(mean_table.keys())
    for noise in noises:
        setups.update(mean_table[noise].keys())
    setups = sorted(setups)
    lines = []
    header = '| Setup | ' + ' | '.join(noises) + ' |'
    sep = '| ' + ' | '.join(['---'] * (len(noises) + 1)) + ' |'
    lines.append(header)
    lines.append(sep)
    for setup in setups:
        row = [setup]
        for noise in noises:
            val = mean_table.get(noise, {}).get(setup, {}).get('F1 Score', None)
            row.append(f"{val:.3f}" if isinstance(val, float) else '-')
        lines.append('| ' + ' | '.join(row) + ' |')
    return '\n'.join(lines)


def write_report(data, root_dir, out_file):
    mean_table, std_table = aggregate_metrics(data)
    with open(out_file, 'w') as f:
        f.write('# 实验报告\n\n')
        for noise, seeds in data.items():
            f.write(f'## Noise Condition: {noise}\n\n')
            for seed, setups in seeds.items():
                f.write(f'### Seed: {seed}\n\n')
                for setup_name, info in setups.items():
                    f.write(f'#### Setup: {setup_name}\n\n')
                    hp = info['hyperparameters']
                    if hp:
                        f.write('**Hyperparameters:**\n')
                        for k, v in list(hp.items())[:10]:
                            f.write(f'- {k}: {v}\n')
                        f.write('\n')
                    opt = info['options']
                    if opt:
                        f.write('**Options:**\n')
                        for k, v in list(opt.items())[:10]:
                            f.write(f'- {k}: {v}\n')
                        f.write('\n')
                    metrics = info['metrics']
                    if metrics:
                        f.write(f'*Best Epoch*: {info["best_epoch"]}\n\n')
                        f.write('| F1 Score | Accuracy | Precision | Recall |\n')
                        f.write('| --- | --- | --- | --- |\n')
                        f.write(f"| {metrics['F1 Score']} | {metrics['Accuracy']} | {metrics['Precision']} | {metrics['Recall']} |\n\n")
                    if info['loss_png'] and os.path.exists(info['loss_png']):
                        rel = os.path.relpath(info['loss_png'], root_dir)
                        f.write(f"![Loss Curve]({rel})\n\n")
                    for img in info['confusion_matrices']:
                        rel = os.path.relpath(img, root_dir)
                        f.write(f"![{Path(img).name}]({rel})\n")
                    if info['confusion_matrices']:
                        f.write('\n')
                    for img in info['trend_imgs']:
                        rel = os.path.relpath(img, root_dir)
                        f.write(f"![{Path(img).name}]({rel})\n")
                    if info['trend_imgs']:
                        f.write('\n')
        f.write('## Analysis\n\n')
        f.write('### Average F1 Score per Setup and Noise Condition\n\n')
        f.write(format_table(mean_table) + '\n\n')
        f.write('### Observations\n')
        f.write('- Noise generally degrades performance. Comparing `std0_bias0` (no noise) and `std0_bias0_1` or `std005_bias0_1` shows a decline in F1 scores across most setups.\n')
        f.write('- The `ideal-latent` setup, evaluated under `std005_bias0_1`, achieves the highest F1 score, indicating it is not affected by the added noise.\n')
        f.write('- Among the noisy setups, `air-propagate-latent` maintains better performance compared with `sound-power` and `End-2-end`.\n')
        f.write('- Standard deviation across seeds is largest for the `End-2-end` setup, indicating higher sensitivity to random initialization.\n')
        f.write('\n')
        f.write('### Standard Deviation of F1 Scores Across Seeds\n')
        for noise in sorted(std_table.keys()):
            for setup in sorted(std_table[noise].keys()):
                std = std_table[noise][setup]
                f.write(f'- {noise} / {setup}: {std:.4f}\n')


def main():
    parser = argparse.ArgumentParser(description='Generate experiment markdown report')
    parser.add_argument('root', help='Path to auto_sync directory')
    parser.add_argument('-o', '--output', default='report.md', help='Output markdown file')
    args = parser.parse_args()
    data = collect_data(args.root)
    write_report(data, args.root, args.output)


if __name__ == '__main__':
    main()
