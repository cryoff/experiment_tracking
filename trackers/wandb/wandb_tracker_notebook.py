import os

import wandb
from langchain_community.callbacks.tracers import WandbTracer


class WandbTrackerForNotebook:
    def __init__(self, project: str, key: str, endpoint: str):
        super().__init__()
        self.project = project
        self.key = key
        self.endpoint = endpoint

        os.environ["LANGCHAIN_WANDB_TRACING"] = "true"
        os.environ["WANDB_PROJECT"] = self.project

        wandb.login(key=self.key,
                    relogin=False,
                    host=self.endpoint,
                    force=False,
                    timeout=60
                    )

    def get(self) -> WandbTracer:
        return WandbTracer()
