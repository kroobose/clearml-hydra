from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import List

# メインの設定クラス
@dataclass
class ExperimentConfig:
    name: str = "default_experiment"
    version: float = 1.0

@dataclass
class TrainConfig:
    batch_size: int = 32
    epochs: int = 10
    learning_rate: float = 0.001

@dataclass
class ModelConfig:
    type: str = "resnet50"
    num_classes: int = 10

@dataclass
class OptimizerConfig:
    type: str = "adam"

@dataclass
class ClearMLConfig:
    project_name: str = "clearml-xxx-project"
    task_name: str = 'hydra-test'
    task_type: str = "training"

@dataclass
class Config:
    experiment: ExperimentConfig = ExperimentConfig()
    train: TrainConfig = TrainConfig()
    model: ModelConfig = ModelConfig()
    optimizer: OptimizerConfig = OptimizerConfig()
    clearml: ClearMLConfig = ClearMLConfig()
