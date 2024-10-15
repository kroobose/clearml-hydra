import hydra
from omegaconf import DictConfig
from hydra.core.config_store import ConfigStore
from configs import Config
from clearml import Task

cs = ConfigStore.instance()
cs.store(name="config", node=Config)

@hydra.main(config_path="../configs", config_name="config", version_base="1.1")
def main(cfg: DictConfig):
    task = Task.init(
        project_name=cfg.clearml.project_name,
        task_name=cfg.clearml.task_name,
        task_type=cfg.clearml.task_type
    )

    print(f"Experiment: {cfg.experiment.name} (version {cfg.experiment.version})")
    print(f"Training for {cfg.train.epochs} epochs with batch size {cfg.train.batch_size}")

    print(f"Using model: {cfg.model.type}")
    print(f"Optimizer: {cfg.optimizer.type}")

if __name__ == "__main__":
    main()
