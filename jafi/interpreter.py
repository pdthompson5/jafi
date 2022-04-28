# I would like to implement currying so functions can be partially evaluated 


from tkinter import E
from expr import *
from visitor import Visitor
from environment import Environment

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
        pass
    
    def visit_variable_declaration(self, expr: VariableDeclaration):
        initializer = self.evaluate(expr.initializer)
        self.env.put(expr.name, initializer)
        return initializer

    
    def visit_variable(self, expr: Variable):
        return self.env.get(expr.name)

    
    def visit_flow(self, expr: Flow):
        pass
    
    def visit_function_call(self, expr: FunctionCall):
        pass


    def visit_literal(self, expr: Literal):
        return expr.literal

    
    def visit_grouping(self, expr: Grouping):
        return self.evaluate(expr.enclosed)