from typing import List

from jafi_callable import JafiCallable


class NativeFunction(JafiCallable):
    def __init__(self, arity: int, function, defined_arguments = []) -> None:
        self.function = function
        self.defined_arguments = defined_arguments
        super().__init__(arity)
    
    def call(self, arguments : List[object], interpreter):
        # currying should be possible for this as well 
        if len(arguments) < self.arity:
            return NativeFunction(self.arity - len(arguments), self.function, arguments)
        else:   
            return self.function(self.defined_arguments + arguments , interpreter)