from datetime import date
from datetime import datetime
import logging
from pathlib import Path
from typing import Literal
from omegaconf import DictConfig, OmegaConf
from pydantic import BaseModel, ConfigDict, DirectoryPath, FilePath
import hydra


class BaseConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True, validate_default=True)


class DataConfig(BaseConfig):
    data_format: Literal["DB", "SAP"]
    input_path: DirectoryPath | FilePath
    start_date: date
    window: int


class ModelConfig(BaseConfig):
    num_estimators: int
    max_depth: int


class ProjectConfig(BaseConfig):
    data: DataConfig
    model: ModelConfig


@hydra.main(version_base=None, config_path="config", config_name="cla")
def main(cla: DictConfig):
    OmegaConf.resolve(cla)
    logging.info("Loaded Config:\n" + OmegaConf.to_yaml(cla))

    cla = ProjectConfig(**cla)
    logging.info(f"cla pydantic: {cla}")

    logging.critical("I am a Critical Message!")
    logging.error("I am an Error Message!")
    logging.warning("I am a Warning Message!")
    logging.debug("I am a Debug Message.")


if __name__ == "__main__":
    main()
