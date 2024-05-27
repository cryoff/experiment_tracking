from langfuse.callback import CallbackHandler

from utils.tracker.experiment_tracker import ExperimentTracker


class LangFuseTracker(ExperimentTracker):
    _instance = None
    # _env_var = EnvCfg.LANGFUSE_SERVER
    service_name = "langfuse"

    def _get_instance(self, config: dict = None) -> CallbackHandler | None:
        # if not config:
        #     return CallbackHandler(
        #         public_key=os.getenv(EnvCfg.LANGFUSE_PUBLIC_KEY.name, EnvCfg.LANGFUSE_PUBLIC_KEY.default),
        #         secret_key=os.getenv(EnvCfg.LANGFUSE_SECRET_KEY.name, EnvCfg.LANGFUSE_SECRET_KEY.default),
        #         host=self._endpoint)
                # host="http://localhost:3000/")
        # else:
        return CallbackHandler(
            public_key=config.get("public_key"),
            secret_key=config.get("secret_key"),
            host=self._endpoint)
