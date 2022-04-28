from jafi_token import Token
from runtime_error import RuntimeError


class Environment:
    
    def __init__(self, enclosing = None, copied_env = None) -> None:
        if not copied_env is None:
            self.env = copied_env
            self.enclosing = enclosing
            return
        self.env = dict()
        self.enclosing = enclosing

    def copy(self): 
        return Environment(self.enclosing, self.env.copy())

    def put(self, token : Token, value: object) -> None:
        name = token.lexeme
        if name in self.env.keys():
            raise RuntimeError(token.line, f"Variable {name} is already defined.")
        self.env[name] = value

    def get(self, token : Token) -> object:
        name = token.lexeme
        if not name in self.env.keys(): 
            if not self.enclosing is None:
                return self.enclosing.get(token)
            else:
                raise RuntimeError(token.line, f"Variable {name} is not defined.")
        return self.env[name]

    def __str__(self):
        string = f"{self.env}"
        if not self.enclosing is None:
            string += self.enclosing.__str__()
        return string