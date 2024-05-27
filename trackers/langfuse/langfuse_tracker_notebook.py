from langfuse.callback import CallbackHandler


class LangFuseTrackerForNotebooks:

    def __init__(self, endpoint: str, public_key: str, secret_key: str):
        self._endpoint = endpoint
        self._public_key = public_key
        self._secret_key = secret_key

    def get(self) -> CallbackHandler | None:
        return CallbackHandler(
            public_key=self._public_key,
            secret_key=self._secret_key,
            host=self._endpoint)
