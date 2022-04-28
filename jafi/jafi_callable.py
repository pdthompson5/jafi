from abc import ABC, abstractmethod
from typing import List
from jafi_token import Token

class JafiCallable(ABC):
    def __init__(self, arity : int) -> None:
        self.arity = arity

    @abstractmethod
    def call(self, arguments : List[object], interpreter, paren: Token) -> object:
        pass

    def arity(self) -> int:
        return self.arity()
