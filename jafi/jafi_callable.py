from abc import ABC, abstractmethod
from typing import List

class JafiCallable(ABC):
    def __init__(self, arity : int) -> None:
        self.arity = arity

    @abstractmethod
    def call(self, arguments : List[object], interpreter) -> object:
        pass

    def arity(self) -> int:
        return self.arity()
