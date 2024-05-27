from langchain.callbacks import StdOutCallbackHandler
from langfuse import Langfuse
from loguru import logger

from utils.tracker.experiment_tracker import ExperimentTracker
from utils.tracker.trackers.langfuse.langfuse_tracker import LangFuseTracker
from utils.tracker.trackers.logurucallback.logger_callback_handler import LoguruInfoCallbackHandler
from utils.tracker.trackers.wandb.wandb_tracker import WandbTracker


# from phoenix.trace.exporter import HttpExporter
# from phoenix.trace.langchain import OpenInferenceTracer, LangChainInstrumentor


class TrackerProvider:
    trackers: list[ExperimentTracker] = []

    @classmethod
    def get_stdout_callback_handler(cls) -> StdOutCallbackHandler:
        return StdOutCallbackHandler()

    @classmethod
    def get_loguru_callback_handler(cls) -> LoguruInfoCallbackHandler:
        return LoguruInfoCallbackHandler()

    # @classmethod
    # def get_phoenix_callback_handler_config(cls) -> OpenInferenceTracer:
    #     exporter = HttpExporter(endpoint="http://localhost:6565")
    #     tracer = OpenInferenceTracer(exporter)
    #     # tracer = OpenInferenceTracer()
    #     LangChainInstrumentor(tracer).instrument()
    #     return tracer

    @classmethod
    def init_with_config(cls, config: dict) -> list[ExperimentTracker]:
        if "trackers" in config:
            for tracker in config["trackers"]:
                tracker_name = tracker.get('name')
                logger.info(f"Initializing tracker: {tracker_name}")
                if 'config' in tracker:
                    print(f"Configuration: {tracker['config']}")
                    tracker_config = tracker['config']

                match tracker_name:
                    case "wandb":
                        if wandb_tracker := WandbTracker(tracker_config):
                            cls.trackers.append(wandb_tracker)
                    case "langfuse":
                        if langfuse := LangFuseTracker(tracker_config):
                            cls.trackers.append(langfuse)
                    # case "phoenix":
                    #     if phoenix := ArizePhoenixTracker(tracker_config):
                    #         cls.trackers.append(phoenix)
                    case "loguru":
                        cls.trackers.append(LoguruInfoCallbackHandler())
                    # case "mlflow":
                    #     if mlflow_tracker := MlFlowTracker(tracker_config):
                    #         cls.trackers.append(mlflow_tracker)

        return cls.trackers


if __name__ == "__main__":
    langfuse = Langfuse(public_key="pk-lf-ee61f1eb-53fc-4e6a-8a1b-68e68d40d0b5",
                        secret_key="sk-lf-c8c32810-6344-4b6b-99ee-11f53070f8bf",
                        host="http://localhost:3000/")
