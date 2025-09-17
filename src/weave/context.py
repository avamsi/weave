from typing import Any


class Context:
    def __init__(self, **kwargs: Any):
        self._values = kwargs

    def get(self, key: str, default: Any = None) -> Any:
        return self._values.get(key, default)
