# I would like to implement currying so functions can be partially evaluated 


from expr import *
from jafi_callable import JafiCallable
from jafi_function import JafiFunction
from visitor import Visitor
from environment import Environment
from runtime_error import RuntimeError
from error_reporting import report_error
from native_function import NativeFunction

class Interpreter(Visitor):
    def __init__(self) -> None:
        standard_env = {
        "+" : NativeFunction(2, lambda a, b: a[0] + a[1]),
        "-" : NativeFunction(2, lambda a, b: a[0] - a[1]),
        "*" : NativeFunction(2, lambda a, b: a[0] * a[1]),
        "/" : NativeFunction(2, lambda a, b: a[0] / a[1]),
        "%" : NativeFunction(2, lambda a, b: a[0] % a[1]),
        }
        self.env = Environment(standard_env)





    def evaluate(self, expr: Expr):
        try: 
            return expr.accept(self)
        except RuntimeError as e:
            report_error(e.message, e.line)


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
            raise RuntimeError(expr.paren.line, f"{left_side} is not callable.")

        argument_values = []
        for argument in expr.arguments:
            argument_values.append(self.evaluate(argument))

        return left_side.call(argument_values, self)


    def visit_literal(self, expr: Literal):
        return expr.literal

    
    def visit_grouping(self, expr: Grouping):
        return self.evaluate(expr.enclosed)