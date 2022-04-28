# I would like to implement currying so functions can be partially evaluated 


from expr import *
from jafi_callable import JafiCallable
from jafi_function import JafiFunction
from visitor import Visitor
from environment import Environment
from runtime_error import RuntimeError

class Interpreter(Visitor):
    def __init__(self) -> None:
        self.env = Environment()


    def evaluate(self, expr: Expr):
        return expr.accept(self)


    def evaluate_function(self, body : Expr, local : Environment):
        old_env = self.env
        self.env = local

        try: 
            val = self.evaluate(body)
        except RuntimeError as e:
            raise e
        finally:
            self.env = old_env
        return val


    def visit_function_declaration(self, expr: FunctionDeclaration):
        function = JafiFunction(expr, self.env)
        self.env.put(expr.name, function)
        return function
    
    def visit_variable_declaration(self, expr: VariableDeclaration):
        initializer = self.evaluate(expr.initializer)
        self.env.put(expr.name, initializer)
        return initializer

    
    def visit_variable(self, expr: Variable):
        return self.env.get(expr.name)

    
    def visit_flow(self, expr: Flow):
        pass
    
    def visit_function_call(self, expr: FunctionCall):
        left_side = self.evaluate(expr.l_value)

        if not isinstance(left_side, JafiCallable):
            raise RuntimeError(expr.paren.line, f"{left_side} is not callable")

        return left_side.call(expr.arguments, self)


    def visit_literal(self, expr: Literal):
        return expr.literal

    
    def visit_grouping(self, expr: Grouping):
        return self.evaluate(expr.enclosed)