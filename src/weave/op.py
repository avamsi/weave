from abc import ABC, abstractmethod

from pyspark.sql import DataFrame

from weave.context import Context


class Op(ABC):
    @abstractmethod
    def inputs(self) -> set[str]: ...

    @abstractmethod
    def outputs(self) -> set[str]: ...

    @abstractmethod
    def run(self, ctx: Context, df: DataFrame) -> DataFrame: ...
