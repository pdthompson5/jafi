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


class CompositeFunction(JafiCallable):
    def __init__(self, arity: int, functions: List[JafiCallable]) -> None:
        self.functions = functions.copy()
        super().__init__(arity)

    def call(self, arguments: List[object], interpreter, paren: Token) -> object:
        current_arguments = arguments

        for function in self.functions:
            return_val = function.call(current_arguments, interpreter, paren)
            current_arguments = [return_val]

        return return_val

    def __str__(self) -> str:
        string = "<"
        for function in self.functions:
            string += f"{function}"
        string += ">"
        return string
