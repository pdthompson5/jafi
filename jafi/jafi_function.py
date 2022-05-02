from typing import List


from .jafi_callable import JafiCallable
from .environment import Environment
from .expr import FunctionDeclaration
from .jafi_token import Token
from .runtime_error import RuntimeError

class JafiFunction(JafiCallable):
    def __init__(self, decl : FunctionDeclaration, closure: Environment, local = None) -> None:
        self.decl = decl
        if not local is None:
            self.local = local
        else:
            self.local = Environment(closure)
        super().__init__(decl.parameters.__len__())


    def call(self, arguments: List[object], interpreter, paren: Token) -> object:
        arity = self.arity
        params = self.decl.parameters.copy()

        env = self.local.copy()
        for argument in arguments:
            if arity == 0: #Too many arguments 
                raise RuntimeError(paren.line, f"Function '{self.decl.name.lexeme}' got {len(arguments)} arguments. Expected: {self.arity}.") 
            env.put(params.pop(0), argument)
            arity -= 1

        if arity == 0:
            #Evaluate the function 
            return interpreter.evaluate_function(self.decl.body, env)
        # Currying -> If this function did not receive enough arguments, return the same function with the given arguments defined 
        else:
            # Create new function declaration without the paramters that have been defined 
            new_decl = FunctionDeclaration(self.decl.name, params, self.decl.body)
            return JafiFunction(new_decl, None, env)
            
    def __str__(self):
        return f"<function {self.decl.name.lexeme}>"

