import requests
from langchain_core.callbacks import BaseCallbackHandler
from loguru import logger
# from phoenix.trace.langchain import OpenInferenceTracer


class ExperimentTracker:
    _instance = None
    _NO_ENV_VAR_DEFINED: str = "None"

    def __new__(cls, config: dict = None):
        if not isinstance(cls._instance, cls) and cls.__name__ != 'LoguruInfoCallbackHandler':
            cls._instance = super(ExperimentTracker, cls).__new__(cls)
            cls._instance._service_name = cls.service_name
            if not config:
                cls._instance = None
                # cls._instance._endpoint = os.getenv(cls._instance._env_var.name, cls._instance._env_var.default)
                # cls._instance._accessible = cls._instance._check_accessible()
                # cls._instance._callback_handler = cls._instance._init()
            else:
                cls._instance._endpoint = config.get('endpoint')
                cls._instance._accessible = cls._instance._check_accessible()
                cls._instance._callback_handler = cls._instance._init(config)
                cls._instance._config = config

        if cls.__name__ == 'LoguruInfoCallbackHandler':
            cls._instance = super(ExperimentTracker, cls).__new__(cls)
            cls._instance._service_name = cls.service_name
            return cls._instance

        if not cls._instance._callback_handler:
            return None

        return cls._instance

    @classmethod
    # def get(cls) -> BaseCallbackHandler | OpenInferenceTracer | None:
    def get(cls) -> BaseCallbackHandler |  None:
        return cls._instance._callback_handler
        # pass

    @classmethod
    # def _get_instance(cls, config: dict = None) -> BaseCallbackHandler | OpenInferenceTracer | None:
    def _get_instance(cls, config: dict = None) -> BaseCallbackHandler |  None:
        pass

    # def _init(self, config: dict = None) -> BaseCallbackHandler | OpenInferenceTracer | None:
    def _init(self, config: dict = None) -> BaseCallbackHandler | None:
        if self._accessible:
            return self._get_instance(config)
        else:
            return None

    def _check_accessible(self) -> bool:
        logger.info(f"Check if {self._service_name} is accessible at {self._endpoint}")
        try:
            response = requests.get(self._endpoint)
            response.raise_for_status()
            logger.info(f"{self._service_name} is accessible at {self._endpoint}")
            return True
        except requests.exceptions.RequestException as err:
            logger.error(f"{self._service_name} is not accessible at {self._service_name}. Error: {err}")
            return False

    def finish(self):
        pass
