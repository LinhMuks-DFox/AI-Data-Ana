# 实验报告

## Noise Condition: std005_bias0_1

### Seed: experiment_seed_114514

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 437

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.3445972507025138 | 0.355 | 0.38676190476190475 | 0.355 |

![Loss Curve](std005_bias0_1/experiment_seed_114514/2025-06-03-10-21-00-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_114514/2025-06-03-10-21-00-sound-power/epoch437/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_114514/2025-06-03-10-21-00-sound-power/epoch437/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_114514/2025-06-03-10-21-00-sound-power/epoch437/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_114514/2025-06-03-10-21-00-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_114514/2025-06-03-10-21-00-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_114514/2025-06-03-10-21-00-sound-power/validate_metrics_trends.png)

#### Setup: ideal-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 151

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.71831746031746 | 0.73 | 0.7572467532467533 | 0.73 |

![Loss Curve](std005_bias0_1/experiment_seed_114514/2025-06-03-11-33-58-ideal-latent/epoch299/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_114514/2025-06-03-11-33-58-ideal-latent/epoch151/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_114514/2025-06-03-11-33-58-ideal-latent/epoch151/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_114514/2025-06-03-11-33-58-ideal-latent/epoch151/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_114514/2025-06-03-11-33-58-ideal-latent/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_114514/2025-06-03-11-33-58-ideal-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_114514/2025-06-03-11-33-58-ideal-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 276

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.27223860350176143 | 0.295 | 0.3382712842712843 | 0.295 |

![Loss Curve](std005_bias0_1/experiment_seed_114514/2025-06-03-13-12-34-End-2-end/epoch299/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_114514/2025-06-03-13-12-34-End-2-end/epoch276/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_114514/2025-06-03-13-12-34-End-2-end/epoch276/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_114514/2025-06-03-13-12-34-End-2-end/epoch276/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_114514/2025-06-03-13-12-34-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_114514/2025-06-03-13-12-34-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_114514/2025-06-03-13-12-34-End-2-end/validate_metrics_trends.png)

### Seed: experiment_seed_3047

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 401

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.3645642135642136 | 0.365 | 0.4081428571428571 | 0.365 |

![Loss Curve](std005_bias0_1/experiment_seed_3047/2025-06-03-02-47-05-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-02-47-05-sound-power/epoch401/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-02-47-05-sound-power/epoch401/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-02-47-05-sound-power/epoch401/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-02-47-05-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-02-47-05-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-02-47-05-sound-power/validate_metrics_trends.png)

#### Setup: ideal-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 231

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.6878138528138527 | 0.705 | 0.7075714285714285 | 0.705 |

![Loss Curve](std005_bias0_1/experiment_seed_3047/2025-06-03-04-02-19-ideal-latent/epoch299/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-02-19-ideal-latent/epoch231/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-02-19-ideal-latent/epoch231/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-02-19-ideal-latent/epoch231/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-02-19-ideal-latent/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-02-19-ideal-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-02-19-ideal-latent/validate_metrics_trends.png)

#### Setup: air-propagate-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 310

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.5105655046707678 | 0.535 | 0.5448571428571429 | 0.535 |

![Loss Curve](std005_bias0_1/experiment_seed_3047/2025-06-03-04-44-56-air-propagate-latent/epoch499/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-44-56-air-propagate-latent/epoch310/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-44-56-air-propagate-latent/epoch310/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-44-56-air-propagate-latent/epoch310/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-44-56-air-propagate-latent/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-44-56-air-propagate-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-04-44-56-air-propagate-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: cpu
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 107

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.24856551683610506 | 0.275 | 0.26184134166487105 | 0.275 |

![Loss Curve](std005_bias0_1/experiment_seed_3047/2025-06-03-05-52-45-End-2-end/epoch499/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-05-52-45-End-2-end/epoch107/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-05-52-45-End-2-end/epoch107/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_3047/2025-06-03-05-52-45-End-2-end/epoch107/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-05-52-45-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-05-52-45-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_3047/2025-06-03-05-52-45-End-2-end/validate_metrics_trends.png)

### Seed: experiment_seed_4999

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 191

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.3244565761036349 | 0.34 | 0.36837057387057387 | 0.34 |

![Loss Curve](std005_bias0_1/experiment_seed_4999/2025-06-03-17-43-11-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-17-43-11-sound-power/epoch191/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-17-43-11-sound-power/epoch191/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-17-43-11-sound-power/epoch191/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-17-43-11-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-17-43-11-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-17-43-11-sound-power/validate_metrics_trends.png)

#### Setup: ideal-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 250

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.7108414134884723 | 0.705 | 0.7847435897435898 | 0.705 |

![Loss Curve](std005_bias0_1/experiment_seed_4999/2025-06-03-18-59-53-ideal-latent/epoch299/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-18-59-53-ideal-latent/epoch250/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-18-59-53-ideal-latent/epoch250/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-18-59-53-ideal-latent/epoch250/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-18-59-53-ideal-latent/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-18-59-53-ideal-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-18-59-53-ideal-latent/validate_metrics_trends.png)

#### Setup: air-propagate-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 154

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.5418975468975469 | 0.555 | 0.5934155844155844 | 0.555 |

![Loss Curve](std005_bias0_1/experiment_seed_4999/2025-06-03-19-37-17-air-propagate-latent/epoch499/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-19-37-17-air-propagate-latent/epoch154/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-19-37-17-air-propagate-latent/epoch154/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-19-37-17-air-propagate-latent/epoch154/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-19-37-17-air-propagate-latent/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-19-37-17-air-propagate-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-19-37-17-air-propagate-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 240

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.4082270774976656 | 0.42 | 0.5055201465201464 | 0.42 |

![Loss Curve](std005_bias0_1/experiment_seed_4999/2025-06-03-20-32-31-End-2-end/epoch299/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-20-32-31-End-2-end/epoch240/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-20-32-31-End-2-end/epoch240/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_4999/2025-06-03-20-32-31-End-2-end/epoch240/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-20-32-31-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-20-32-31-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_4999/2025-06-03-20-32-31-End-2-end/validate_metrics_trends.png)

### Seed: experiment_seed_65536

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 240

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.30997030747030746 | 0.335 | 0.35424999999999995 | 0.335 |

![Loss Curve](std005_bias0_1/experiment_seed_65536/2025-06-03-13-52-18-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-13-52-18-sound-power/epoch240/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-13-52-18-sound-power/epoch240/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-13-52-18-sound-power/epoch240/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-13-52-18-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-13-52-18-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-13-52-18-sound-power/validate_metrics_trends.png)

#### Setup: ideal-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 144

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.6199036519036519 | 0.635 | 0.6768650793650793 | 0.635 |

![Loss Curve](std005_bias0_1/experiment_seed_65536/2025-06-03-15-13-33-ideal-latent/epoch299/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-13-33-ideal-latent/epoch144/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-13-33-ideal-latent/epoch144/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-13-33-ideal-latent/epoch144/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-13-33-ideal-latent/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-13-33-ideal-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-13-33-ideal-latent/validate_metrics_trends.png)

#### Setup: air-propagate-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 129

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.49020456667515494 | 0.515 | 0.5267690642690642 | 0.515 |

![Loss Curve](std005_bias0_1/experiment_seed_65536/2025-06-03-15-55-45-air-propagate-latent/epoch499/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-55-45-air-propagate-latent/epoch129/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-55-45-air-propagate-latent/epoch129/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-55-45-air-propagate-latent/epoch129/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-55-45-air-propagate-latent/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-55-45-air-propagate-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-15-55-45-air-propagate-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 241

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.3019550040602672 | 0.325 | 0.3433679653679653 | 0.325 |

![Loss Curve](std005_bias0_1/experiment_seed_65536/2025-06-03-16-59-18-End-2-end/epoch299/loss.png)

![test_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-16-59-18-End-2-end/epoch241/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-16-59-18-End-2-end/epoch241/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std005_bias0_1/experiment_seed_65536/2025-06-03-16-59-18-End-2-end/epoch241/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-16-59-18-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-16-59-18-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std005_bias0_1/experiment_seed_65536/2025-06-03-16-59-18-End-2-end/validate_metrics_trends.png)

## Noise Condition: std0_bias0

### Seed: experiment_seed_114514

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 374

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.40975901875901877 | 0.43 | 0.4480793650793651 | 0.43 |

![Loss Curve](std0_bias0/experiment_seed_114514/2025-06-03-09-33-29-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_114514/2025-06-03-09-33-29-sound-power/epoch374/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_114514/2025-06-03-09-33-29-sound-power/epoch374/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_114514/2025-06-03-09-33-29-sound-power/epoch374/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_114514/2025-06-03-09-33-29-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_114514/2025-06-03-09-33-29-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_114514/2025-06-03-09-33-29-sound-power/validate_metrics_trends.png)

#### Setup: air-propagate-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 156

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.6520753690753689 | 0.67 | 0.6942568542568543 | 0.67 |

![Loss Curve](std0_bias0/experiment_seed_114514/2025-06-03-10-49-19-air-propagate-latent/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_114514/2025-06-03-10-49-19-air-propagate-latent/epoch156/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_114514/2025-06-03-10-49-19-air-propagate-latent/epoch156/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_114514/2025-06-03-10-49-19-air-propagate-latent/epoch156/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_114514/2025-06-03-10-49-19-air-propagate-latent/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_114514/2025-06-03-10-49-19-air-propagate-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_114514/2025-06-03-10-49-19-air-propagate-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 252

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.38794851008263564 | 0.42 | 0.44460877684407096 | 0.42 |

![Loss Curve](std0_bias0/experiment_seed_114514/2025-06-03-11-51-55-End-2-end/epoch252/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_114514/2025-06-03-11-51-55-End-2-end/epoch252/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_114514/2025-06-03-11-51-55-End-2-end/epoch252/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_114514/2025-06-03-11-51-55-End-2-end/epoch252/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_114514/2025-06-03-11-51-55-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_114514/2025-06-03-11-51-55-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_114514/2025-06-03-11-51-55-End-2-end/validate_metrics_trends.png)

### Seed: experiment_seed_3047

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 407

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.4014676048589092 | 0.425 | 0.4373830409356725 | 0.425 |

![Loss Curve](std0_bias0/experiment_seed_3047/2025-06-03-02-44-17-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_3047/2025-06-03-02-44-17-sound-power/epoch407/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_3047/2025-06-03-02-44-17-sound-power/epoch407/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_3047/2025-06-03-02-44-17-sound-power/epoch407/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_3047/2025-06-03-02-44-17-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_3047/2025-06-03-02-44-17-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_3047/2025-06-03-02-44-17-sound-power/validate_metrics_trends.png)

#### Setup: air-propagate-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 142

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.634996003996004 | 0.65 | 0.6649841269841269 | 0.65 |

![Loss Curve](std0_bias0/experiment_seed_3047/2025-06-03-03-55-27-air-propagate-latent/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_3047/2025-06-03-03-55-27-air-propagate-latent/epoch142/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_3047/2025-06-03-03-55-27-air-propagate-latent/epoch142/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_3047/2025-06-03-03-55-27-air-propagate-latent/epoch142/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_3047/2025-06-03-03-55-27-air-propagate-latent/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_3047/2025-06-03-03-55-27-air-propagate-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_3047/2025-06-03-03-55-27-air-propagate-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: cpu
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 233

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.52899555999556 | 0.525 | 0.6032142857142857 | 0.525 |

![Loss Curve](std0_bias0/experiment_seed_3047/2025-06-03-04-58-31-End-2-end/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_3047/2025-06-03-04-58-31-End-2-end/epoch233/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_3047/2025-06-03-04-58-31-End-2-end/epoch233/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_3047/2025-06-03-04-58-31-End-2-end/epoch233/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_3047/2025-06-03-04-58-31-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_3047/2025-06-03-04-58-31-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_3047/2025-06-03-04-58-31-End-2-end/validate_metrics_trends.png)

### Seed: experiment_seed_4999

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 140

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.40924819624819625 | 0.43 | 0.4718333333333334 | 0.43 |

![Loss Curve](std0_bias0/experiment_seed_4999/2025-06-03-15-34-06-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_4999/2025-06-03-15-34-06-sound-power/epoch140/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_4999/2025-06-03-15-34-06-sound-power/epoch140/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_4999/2025-06-03-15-34-06-sound-power/epoch140/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_4999/2025-06-03-15-34-06-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_4999/2025-06-03-15-34-06-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_4999/2025-06-03-15-34-06-sound-power/validate_metrics_trends.png)

#### Setup: air-propagate-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 142

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.6673842823842823 | 0.675 | 0.7273174603174604 | 0.675 |

![Loss Curve](std0_bias0/experiment_seed_4999/2025-06-03-16-50-45-air-propagate-latent/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_4999/2025-06-03-16-50-45-air-propagate-latent/epoch142/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_4999/2025-06-03-16-50-45-air-propagate-latent/epoch142/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_4999/2025-06-03-16-50-45-air-propagate-latent/epoch142/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_4999/2025-06-03-16-50-45-air-propagate-latent/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_4999/2025-06-03-16-50-45-air-propagate-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_4999/2025-06-03-16-50-45-air-propagate-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 81

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.5223818403818404 | 0.515 | 0.6614573875527222 | 0.515 |

![Loss Curve](std0_bias0/experiment_seed_4999/2025-06-03-17-55-20-End-2-end/epoch299/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_4999/2025-06-03-17-55-20-End-2-end/epoch81/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_4999/2025-06-03-17-55-20-End-2-end/epoch81/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_4999/2025-06-03-17-55-20-End-2-end/epoch81/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_4999/2025-06-03-17-55-20-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_4999/2025-06-03-17-55-20-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_4999/2025-06-03-17-55-20-End-2-end/validate_metrics_trends.png)

### Seed: experiment_seed_65536

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 230

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.36974675324675316 | 0.385 | 0.4091428571428571 | 0.385 |

![Loss Curve](std0_bias0/experiment_seed_65536/2025-06-03-12-28-13-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_65536/2025-06-03-12-28-13-sound-power/epoch230/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_65536/2025-06-03-12-28-13-sound-power/epoch230/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_65536/2025-06-03-12-28-13-sound-power/epoch230/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_65536/2025-06-03-12-28-13-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_65536/2025-06-03-12-28-13-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_65536/2025-06-03-12-28-13-sound-power/validate_metrics_trends.png)

#### Setup: air-propagate-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 186

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.6608498168498168 | 0.665 | 0.7546363636363637 | 0.665 |

![Loss Curve](std0_bias0/experiment_seed_65536/2025-06-03-13-49-58-air-propagate-latent/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_65536/2025-06-03-13-49-58-air-propagate-latent/epoch186/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_65536/2025-06-03-13-49-58-air-propagate-latent/epoch186/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_65536/2025-06-03-13-49-58-air-propagate-latent/epoch186/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_65536/2025-06-03-13-49-58-air-propagate-latent/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_65536/2025-06-03-13-49-58-air-propagate-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_65536/2025-06-03-13-49-58-air-propagate-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 278

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.5468296148296149 | 0.56 | 0.6432662337662337 | 0.56 |

![Loss Curve](std0_bias0/experiment_seed_65536/2025-06-03-14-54-40-End-2-end/epoch299/loss.png)

![test_confusion_matrix_fig.png](std0_bias0/experiment_seed_65536/2025-06-03-14-54-40-End-2-end/epoch278/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0/experiment_seed_65536/2025-06-03-14-54-40-End-2-end/epoch278/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0/experiment_seed_65536/2025-06-03-14-54-40-End-2-end/epoch278/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0/experiment_seed_65536/2025-06-03-14-54-40-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0/experiment_seed_65536/2025-06-03-14-54-40-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0/experiment_seed_65536/2025-06-03-14-54-40-End-2-end/validate_metrics_trends.png)

## Noise Condition: std0_bias0_1

### Seed: experiment_seed_114514

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 324

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.36548773448773453 | 0.4 | 0.3849189144189144 | 0.4 |

![Loss Curve](std0_bias0_1/experiment_seed_114514/2025-06-04-03-53-55-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_114514/2025-06-04-03-53-55-sound-power/epoch324/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_114514/2025-06-04-03-53-55-sound-power/epoch324/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_114514/2025-06-04-03-53-55-sound-power/epoch324/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0_1/experiment_seed_114514/2025-06-04-03-53-55-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0_1/experiment_seed_114514/2025-06-04-03-53-55-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0_1/experiment_seed_114514/2025-06-04-03-53-55-sound-power/validate_metrics_trends.png)

#### Setup: air-propagate-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 126

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.6813268953268953 | 0.695 | 0.724920634920635 | 0.695 |

![Loss Curve](std0_bias0_1/experiment_seed_114514/2025-06-04-05-03-10-air-propagate-latent/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-03-10-air-propagate-latent/epoch126/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-03-10-air-propagate-latent/epoch126/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-03-10-air-propagate-latent/epoch126/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-03-10-air-propagate-latent/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-03-10-air-propagate-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-03-10-air-propagate-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 272

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.15519788013405036 | 0.22 | 0.17059814872549303 | 0.22 |

![Loss Curve](std0_bias0_1/experiment_seed_114514/2025-06-04-05-54-35-End-2-end/epoch299/loss.png)

![test_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-54-35-End-2-end/epoch272/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-54-35-End-2-end/epoch272/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-54-35-End-2-end/epoch272/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-54-35-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-54-35-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0_1/experiment_seed_114514/2025-06-04-05-54-35-End-2-end/validate_metrics_trends.png)

### Seed: experiment_seed_3047

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 445

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.3603308913308913 | 0.39 | 0.39125685425685425 | 0.39 |

![Loss Curve](std0_bias0_1/experiment_seed_3047/2025-06-04-01-08-34-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_3047/2025-06-04-01-08-34-sound-power/epoch445/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_3047/2025-06-04-01-08-34-sound-power/epoch445/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_3047/2025-06-04-01-08-34-sound-power/epoch445/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0_1/experiment_seed_3047/2025-06-04-01-08-34-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0_1/experiment_seed_3047/2025-06-04-01-08-34-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0_1/experiment_seed_3047/2025-06-04-01-08-34-sound-power/validate_metrics_trends.png)

#### Setup: air-propagate-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 176

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.6596704406704406 | 0.675 | 0.7084660894660896 | 0.675 |

![Loss Curve](std0_bias0_1/experiment_seed_3047/2025-06-04-02-21-23-air-propagate-latent/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_3047/2025-06-04-02-21-23-air-propagate-latent/epoch176/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_3047/2025-06-04-02-21-23-air-propagate-latent/epoch176/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_3047/2025-06-04-02-21-23-air-propagate-latent/epoch176/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0_1/experiment_seed_3047/2025-06-04-02-21-23-air-propagate-latent/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0_1/experiment_seed_3047/2025-06-04-02-21-23-air-propagate-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0_1/experiment_seed_3047/2025-06-04-02-21-23-air-propagate-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 285

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.1827167317777074 | 0.205 | 0.26514521111072836 | 0.205 |

![Loss Curve](std0_bias0_1/experiment_seed_3047/2025-06-04-03-16-05-End-2-end/epoch299/loss.png)

![test_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_3047/2025-06-04-03-16-05-End-2-end/epoch285/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_3047/2025-06-04-03-16-05-End-2-end/epoch285/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_3047/2025-06-04-03-16-05-End-2-end/epoch285/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0_1/experiment_seed_3047/2025-06-04-03-16-05-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0_1/experiment_seed_3047/2025-06-04-03-16-05-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0_1/experiment_seed_3047/2025-06-04-03-16-05-End-2-end/validate_metrics_trends.png)

### Seed: experiment_seed_65536

#### Setup: sound-power

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- AudioSampleRate: 44100
- ResampleTo: 16000
- WarmpUp: 10
- MaxLossOfVisualization: 10
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.001, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 445

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.3257132867132867 | 0.36 | 0.34300793650793643 | 0.36 |

![Loss Curve](std0_bias0_1/experiment_seed_65536/2025-06-04-06-29-39-sound-power/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_65536/2025-06-04-06-29-39-sound-power/epoch445/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_65536/2025-06-04-06-29-39-sound-power/epoch445/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_65536/2025-06-04-06-29-39-sound-power/epoch445/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0_1/experiment_seed_65536/2025-06-04-06-29-39-sound-power/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0_1/experiment_seed_65536/2025-06-04-06-29-39-sound-power/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0_1/experiment_seed_65536/2025-06-04-06-29-39-sound-power/validate_metrics_trends.png)

#### Setup: air-propagate-latent

**Hyperparameters:**
- N_Classes: 50
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}
- Epochs: None

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 131

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.6678932178932178 | 0.68 | 0.724969696969697 | 0.68 |

![Loss Curve](std0_bias0_1/experiment_seed_65536/2025-06-04-07-37-06-air-propagate-latent/epoch499/loss.png)

![test_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_65536/2025-06-04-07-37-06-air-propagate-latent/epoch131/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_65536/2025-06-04-07-37-06-air-propagate-latent/epoch131/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_65536/2025-06-04-07-37-06-air-propagate-latent/epoch131/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0_1/experiment_seed_65536/2025-06-04-07-37-06-air-propagate-latent/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0_1/experiment_seed_65536/2025-06-04-07-37-06-air-propagate-latent/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0_1/experiment_seed_65536/2025-06-04-07-37-06-air-propagate-latent/validate_metrics_trends.png)

#### Setup: End-2-end

**Hyperparameters:**
- N_Classes: 50
- N_MIC: 5
- AudioDuration: 5
- WarmpUp: 10
- MaxLossOfVisualization: 10
- AudioSampleRate: 44100
- LearningRate: 0.001
- WeightDecay: 5e-05
- ReduceLROnPlateauMetricsName: validate_loss
- SchedulerParameter: {'gamma': 0.1, 'milestones': [40, 80]}

**Options:**
- CacheSize: 2000
- Device: None
- TrainID: None
- SaveDirectory: None
- CompileModel: False
- BASE_DIR: None
- DataSetPath: None
- TrainSetPath: None
- TestSetPath: None
- ValidatePath: None

*Best Epoch*: 127

| F1 Score | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| 0.40638600288600296 | 0.44 | 0.4935432527242872 | 0.44 |

![Loss Curve](std0_bias0_1/experiment_seed_65536/2025-06-04-08-30-35-End-2-end/epoch299/loss.png)

![test_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_65536/2025-06-04-08-30-35-End-2-end/epoch127/test_confusion_matrix_fig.png)
![train_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_65536/2025-06-04-08-30-35-End-2-end/epoch127/train_confusion_matrix_fig.png)
![validate_confusion_matrix_fig.png](std0_bias0_1/experiment_seed_65536/2025-06-04-08-30-35-End-2-end/epoch127/validate_confusion_matrix_fig.png)

![test_metrics_trends.png](std0_bias0_1/experiment_seed_65536/2025-06-04-08-30-35-End-2-end/test_metrics_trends.png)
![train_metrics_trends.png](std0_bias0_1/experiment_seed_65536/2025-06-04-08-30-35-End-2-end/train_metrics_trends.png)
![validate_metrics_trends.png](std0_bias0_1/experiment_seed_65536/2025-06-04-08-30-35-End-2-end/validate_metrics_trends.png)

## Analysis

### Average F1 Score per Setup and Noise Condition

| Setup | std005_bias0_1 | std0_bias0 | std0_bias0_1 |
| --- | --- | --- | --- |
| End-2-end | 0.308 | 0.497 | 0.248 |
| air-propagate-latent | 0.514 | 0.654 | 0.670 |
| ideal-latent | 0.684 | - | - |
| sound-power | 0.336 | 0.398 | 0.351 |

### Observations
- Noise generally degrades performance. Comparing `std0_bias0` (no noise) and `std0_bias0_1` or `std005_bias0_1` shows a decline in F1 scores across most setups.
- The `ideal-latent` setup, evaluated under `std005_bias0_1`, achieves the highest F1 score, indicating it is not affected by the added noise.
- Among the noisy setups, `air-propagate-latent` maintains better performance compared with `sound-power` and `End-2-end`.
- Standard deviation across seeds is largest for the `End-2-end` setup, indicating higher sensitivity to random initialization.

### Standard Deviation of F1 Scores Across Seeds
- std005_bias0_1 / End-2-end: 0.0718
- std005_bias0_1 / air-propagate-latent: 0.0267
- std005_bias0_1 / ideal-latent: 0.0435
- std005_bias0_1 / sound-power: 0.0239
- std0_bias0 / End-2-end: 0.0771
- std0_bias0 / air-propagate-latent: 0.0299
- std0_bias0 / sound-power: 0.0256
- std0_bias0_1 / End-2-end: 0.1237
- std0_bias0_1 / air-propagate-latent: 0.0212
- std0_bias0_1 / sound-power: 0.0237
