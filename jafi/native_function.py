from typing import List



from .jafi_callable import JafiCallable
from .runtime_error import RuntimeError
from .jafi_token import Token


class NativeFunction(JafiCallable):
    def __init__(self, name, arity: int, function, defined_arguments = []) -> None:
        self.name = name
        self.function = function
        self.defined_arguments = defined_arguments
        super().__init__(arity)
    
    def call(self, arguments : List[object], interpreter, paren : Token):
        if len(arguments) < self.arity: # currying
            return NativeFunction(self.name, self.arity - len(arguments), self.function, arguments)
        else:   
            true_arguments = self.defined_arguments + arguments
            if self.arity == -1 or len(arguments) == self.arity:
                return self.function(self.defined_arguments + arguments , interpreter)
            else:
                raise RuntimeError(paren.line, f"Function '{self.name}' got {len(true_arguments)} arguments. Expected: {self.arity}.")
    
    def __str__(self):
        return f"<function {self.name}>"