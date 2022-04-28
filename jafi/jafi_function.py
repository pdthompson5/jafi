from typing import List
from jafi_callable import JafiCallable
from environment import Environment
from expr import FunctionDeclaration
from jafi_token import Token
from runtime_error import RuntimeError



# This will be one of the most important files. What do I need?
"""
Should you be able to define arguments in reverse? 
    That would be cool. maybe +(' 1)
Currying -> +(1) returns a function object with one of the arguments defined 
    Each function can have its own environment, 
    When it is called the call function defines arguments
    If it reaches the end of the required arguments then it is evaluated
    Otherwise a new function with the pre-defined environment is returned 
Functions as first class objects -> That is mostly handled elsewhere 
Native function should probably just be stored with function objects 


I don't want functions to be able to access global variables so the only enclosing environment is the standard library?
    What about calling other functions? 
        That is a good point. I've changed my mind. Accessing global variables is fine 

"""
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

