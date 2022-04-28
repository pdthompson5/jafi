from jafi_token import Token
from runtime_error import RuntimeError


class Environment:
    
    def __init__(self, enclosing = None) -> None:
        self.env = dict()
        self.enclosing = enclosing

    def put(self, token : Token, value: object) -> None:
        name = token.lexeme
        if name in self.env.keys():
            raise RuntimeError(token.line, f"Variable {name} is already defined.")
        self.env[name] = value

    def get(self, token : Token) -> object:
        name = token.lexeme
        if not name in self.env.keys(): 
            if not self.enclosing is None:
                self.enclosing.get(token)
            else:
                raise RuntimeError(token.line, f"Variable {name} is not defined.")
        return self.env[name]