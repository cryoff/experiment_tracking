import os

import wandb
from langchain_community.callbacks.tracers import WandbTracer
from langchain_community.callbacks.tracers.wandb import WandbRunArgs
from loguru import logger

from utils.tracker.experiment_tracker import ExperimentTracker


class WandbTracker(ExperimentTracker):
    service_name = "wandb"
    _instance = None

    def _get_instance(self, config: dict = None) -> WandbTracer:
        os.environ["LANGCHAIN_WANDB_TRACING"] = "true"
        os.environ["WANDB_PROJECT"] = config["project"]  # "test-notification-summary-poc"

        wandb.login(key=config["key"],  # "local-db87d038cb9e746d84dd7445487ba34315803474",
                    relogin=False,
                    host=config["endpoint"],
                    force=False,
                    timeout=60
                    )
        local_storage_folder = config["local_storage_folder"] if "local_storage_folder" in config else "./utils/tracker/trackers/wandb/wandb_runs"
        run_args: WandbRunArgs = WandbRunArgs(dir=local_storage_folder)
        return WandbTracer(run_args)

    def finish(self):
        wandb.finish()
        logger.info(f"wandb finished")
