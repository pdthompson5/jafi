from expr import *
from jafi_callable import JafiCallable
from jafi_function import JafiFunction
from visitor import Visitor
from environment import Environment
from runtime_error import RuntimeError
from error_reporting import report_error
from native_function import NativeFunction

import standard_lib

class Interpreter(Visitor):
    def __init__(self) -> None:
        standard_env = {
        # Arithmetic
        "+" : NativeFunction("+", 2, lambda a, b: a[0] + a[1]),
        "-" : NativeFunction("-", 2, lambda a, b: a[0] - a[1]),
        "*" : NativeFunction("*", 2, lambda a, b: a[0] * a[1]),
        "/" : NativeFunction("/", 2, lambda a, b: a[0] / a[1]),
        "%" : NativeFunction("%", 2, lambda a, b: a[0] % a[1]),

        # Comparsions 
        ">" : NativeFunction(">", 2, lambda a, b: a[0] > a[1]),
        "<" : NativeFunction("<", 2, lambda a, b: a[0] < a[1]),
        ">=" : NativeFunction(">=", 2, lambda a, b: a[0] >= a[1]),
        "<=" : NativeFunction("<=", 2, lambda a, b: a[0] <= a[1]),
        "eq" : NativeFunction("%", 2, lambda a, b: a[0] == a[1]),
        
        # Data structures
        "list" : NativeFunction("list", -1, lambda a, b: a),
        "tuple" : NativeFunction("tuple", -1, lambda a, b: tuple(a)),
        "dict"  : NativeFunction("dict", -1, lambda a, b: dict(a)),

        # Data structure management 
        "head" : NativeFunction("head", 1, lambda a, b: a[0][0]),
        "tail" : NativeFunction("tail", 1, lambda a, b: a[0][len(a[0])-1]),
        "index" : NativeFunction("index", 2, lambda a, b: a[0][int(a[1])]),
        "look_up" : NativeFunction("look_up", 2, lambda a, b: a[0][a[1]]),
        "cons" : NativeFunction("cons", 2, lambda a, b: [a[0]] + a[1]),

        # Add -> Replace, delete, maybe more


        # Functional paradigm functions
        "map" : NativeFunction("map", 2, standard_lib.map),
        "filter" : NativeFunction("filter", 2, standard_lib.filter),
        "reduce" : NativeFunction("reduce", 3, standard_lib.reduce)

        }
        self.env = Environment(standard_env)


# In order to implement control flow as native functions I would need lazy evaluation 
# Flow control is next up, I need that before I can make anything useful 


    def evaluate(self, expr: Expr):
        try: 
            return expr.accept(self)
        except RuntimeError as e:
            report_error(e.message, e.line)
            raise e


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

        return left_side.call(argument_values, self, expr.paren)
    
    def visit_if_expr(self, expr: IfExpr):
        condition = self.evaluate(expr.condition)
        if condition:
            return self.evaluate(expr.if_true)
        else:
            return self.evaluate(expr.else_clause)


    def visit_literal(self, expr: Literal):
        return expr.literal

    
    def visit_grouping(self, expr: Grouping):
        return self.evaluate(expr.enclosed)


    def is_char_list(value):
        return len(value) > 0 and isinstance(value[0], str) and len([x for x in value if len(x) > 1]) == 0

    def stringify(value: object):
        if isinstance(value, list):
            if Interpreter.is_char_list(value):
                return "".join([x for x in value])
        return f"{value}"