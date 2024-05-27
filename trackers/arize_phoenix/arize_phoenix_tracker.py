from phoenix.trace.exporter import HttpExporter
from phoenix.trace.langchain import OpenInferenceTracer, LangChainInstrumentor

from utils.tracker.experiment_tracker import ExperimentTracker


class ArizePhoenixTracker(ExperimentTracker):
    # _env_var = EnvCfg.PHOENIX_SERVER
    service_name = "phoenix"
    _tracker: ExperimentTracker = None

    def _get_instance(self, config: dict = None) -> OpenInferenceTracer:
        exporter = HttpExporter(endpoint=self._endpoint)
        tracer = OpenInferenceTracer(exporter)
        # tracer = OpenInferenceTracer()
        LangChainInstrumentor(tracer).instrument()
        return tracer
 