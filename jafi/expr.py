
from abc import ABC, abstractmethod
from typing import List
from jafi_token import Token 

class Expr(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class FunctionDeclaration(Expr):
    def __init__(self, name : Token, parameters : List[Token], body : Expr, ):
        self.name = name
        self.parameters = parameters
        self.body = body
    def accept(self, visitor):
        return visitor.visit_function_declaration(self)

class VariableDeclaration(Expr):
    def __init__(self, name : Token, initializer : Expr, ):
        self.name = name
        self.initializer = initializer
    def accept(self, visitor):
        return visitor.visit_variable_declaration(self)

class Variable(Expr):
    def __init__(self, name : Token, ):
        self.name = name
    def accept(self, visitor):
        return visitor.visit_variable(self)

class Literal(Expr):
    def __init__(self, literal : object, ):
        self.literal = literal
    def accept(self, visitor):
        return visitor.visit_literal(self)

class Grouping(Expr):
    def __init__(self, paren : Token, enclosed : Expr, ):
        self.paren = paren
        self.enclosed = enclosed
    def accept(self, visitor):
        return visitor.visit_grouping(self)

class Flow(Expr):
    def __init__(self, keyword : Token, starting_val : Expr, body : List[Expr], ):
        self.keyword = keyword
        self.starting_val = starting_val
        self.body = body
    def accept(self, visitor):
        return visitor.visit_flow(self)

class FunctionCall(Expr):
    def __init__(self, l_value : Expr, arguments : List[Expr], ):
        self.l_value = l_value
        self.arguments = arguments
    def accept(self, visitor):
        return visitor.visit_function_call(self)

