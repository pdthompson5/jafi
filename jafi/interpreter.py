from math import floor
from .expr import *
from .jafi_callable import JafiCallable
from .jafi_function import JafiFunction
from .visitor import Visitor
from .environment import Environment
from .runtime_error import RuntimeError
from .error_reporting import report_error
from .native_function import NativeFunction

from . import standard_lib

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
        "eq" : NativeFunction("eq", 2, lambda a, b: a[0] == a[1]),
        "not_eq" : NativeFunction("not_eq", 2, lambda a, b: not (a[0] == a[1])),
        "pow" : NativeFunction("pow", 2, lambda a, b: pow(a[0], a[1])),

        #logical operators
        "not" : NativeFunction("not", 1, lambda a, b: not a[0]),
        "and" : NativeFunction("and", 2, lambda a, b:  a[0] and a[1]),
        "or" : NativeFunction("or", 2, lambda a, b: a[0] or a[1]),

        
        # Data structures
        "list" : NativeFunction("list", -1, lambda a, b: a),
        "tuple" : NativeFunction("tuple", -1, lambda a, b: tuple(a)),
        "dict"  : NativeFunction("dict", -1, lambda a, b: dict(a)),

        # Data structure management 
        "head" : NativeFunction("head", 1, lambda a, b: a[0][0]),
        "tail" : NativeFunction("tail", 1, lambda a, b: a[0][1:]),
        "index" : NativeFunction("index", 2, lambda a, b: a[0][int(a[1])]),
        "look_up" : NativeFunction("look_up", 2, lambda a, b: a[0][a[1]]),
        "cons" : NativeFunction("cons", 2, lambda a, b: [a[0]] + a[1]),
        "elem" : NativeFunction("elem", 2, lambda a, b: a[0] in a[1]),
        "len" : NativeFunction("len", 1, lambda a, b: len(a[0])),
    


        # Functional paradigm functions
        "map" : NativeFunction("map", 2, standard_lib.map),
        "filter" : NativeFunction("filter", 2, standard_lib.filter),
        "reduce" : NativeFunction("reduce", 3, standard_lib.reduce),
        "compose" : NativeFunction("compose", -1, standard_lib.compose),

        
        "to_lower" : NativeFunction("to_lower", 1, standard_lib.to_lower),
        }
        self.env = Environment(standard_env)


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
    
    def visit_lambda_expr(self, expr: LambdaExpr):
        return JafiFunction(expr, self.env)
    
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
        if is_char_list(value):
            return "\"" + "".join([x for x in value]) + "\""
        return "[" + ", ".join([stringify(x) for x in value])  + "]"
    if isinstance(value, float):
        value_str = str(value)
        if value_str[len(value_str)-2:] == ".0":
            return value_str[0:len(value_str)-2]
    return value

# Python types to jafi types 
def to_jafi(value: object):
    if isinstance(value, int):
        return float(value)
    if isinstance(value, str):
        return list(value)
    if isinstance(value, list):
        return [to_jafi(x) for x in value]
    return value

# Jafi types to python types
def to_python(value: object):
    if isinstance(value, list):
        if is_char_list(value):
            return "".join([x for x in value])
        return [to_python(x) for x in value]
    if isinstance(value, float):
        if value - floor(value) < 0.00001:
            return floor(value)
    return value