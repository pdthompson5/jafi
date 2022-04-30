"""
FunctionDeclaration
    name: Token 
    parameters: List[Token]
    body: Expr
VariableDeclaration
    name: Token
    initializer: Expr
FunctionCall
    paren: Token 
    callee : Expr
    arguments : List[Expr]
Variable
    name: Token 
Literal
    literal: Token 
Grouping
    paren: Token
    enclosed: Expr
Flow
    keyword: Token 
    starting_values: List[Expr]
    body: List[Expr]
"""

import os


 
my_dict = {
    "FunctionDeclaration" : {"name": "Token", "parameters" : "List[Token]", "body" : "Expr"},
    "LambdaExpr" : {"name" : "Token", "parameters" : "List[Token]", "body" : "Expr"},
    "VariableDeclaration" : {"name": "Token", "initializer" : "Expr"},
    "Variable" : {"name": "Token"},
    "Literal" : {"literal": "object"},
    "Grouping" : {"paren": "Token", "enclosed" : "Expr"},
    "Flow" : {"keyword": "Token", "starting_val" : "Expr", "body" : "List[Expr]"},
    "FunctionCall" : {"paren" : "Token", "l_value" : "Expr", "arguments" : "List[Expr]"},
    "IfExpr" : {"keyword" : "Token", "condition" : "Expr", "if_true" : "Expr", "else_clause" : "Expr"},
}

os.remove("jafi/expr.py")
expr_file = open("jafi/expr.py", "x")


expr_header = """
from abc import ABC, abstractmethod
from typing import List
from jafi_token import Token 

class Expr(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

"""


def create_init(name: str, params: dict) -> str:
    init = "    def __init__(self, "
    for param, type in params.items():
        init += f"{param} : {type}, "
    init += "):\n"

    for param in params.keys():
        init += f"        self.{param} = {param}\n"

    return init

def camel_to_snake(name: str):
    snake = ""
    indices = []
    for i, c in enumerate(name):
        if c.isupper():
            indices.append(i)

    prev_index = 0
    if name[0].isupper():
        snake += name[0].lower()
        indices = indices[1:]
        prev_index += 1

    for index in indices:
        snake += name[prev_index:index]
        snake += f"_{name[index].lower()}"
        prev_index = index+1
    
    snake += name[prev_index:]
    return snake

def create_accept(name:str) -> str:
    accept = "    def accept(self, visitor):\n"
    accept += f"        return visitor.visit_{camel_to_snake(name)}(self)\n"
    return accept
    
def create_expr_class(name: str, params: dict):
    expr = ""
    expr += f"class {name}(Expr):\n"
    expr += create_init(name, params)
    expr += create_accept(name)

    return expr
    
def create_visitor(expr_dict: dict) -> str:
    visitor = "class Visitor(ABC):\n"
    for expr in my_dict.keys():
        visitor += "    @abstractmethod\n"
        visitor += f"    def visit_{camel_to_snake(expr)}(self, expr: {expr}):\n"
        visitor += f"        pass\n\n"
    return visitor 


expr_file.write(expr_header)
for expr, params in my_dict.items():
    expr_file.write(create_expr_class(expr, params))
    expr_file.write("\n")

visitor_header = """
from abc import ABC, abstractmethod
from expr import *
"""
os.remove("jafi/visitor.py")
visitor_file = open("jafi/visitor.py", "x")

visitor_file.write(visitor_header)
visitor_file.write(create_visitor(my_dict))

