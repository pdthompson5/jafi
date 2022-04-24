
from abc import ABC, abstractmethod
from typing import List
from jafi_token import Token 

class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

class FunctionDeclaration(Expr):
    def __init__(self, name : Token, parameters : List[Token], body : Expr, ):
        self.name = name
        self.parameters = parameters
        self.body = body
    def accept(self, visitor : Visitor):
        visitor.visit_function_declaration(self)

class VariableDeclaration(Expr):
    def __init__(self, name : Token, initializer : Expr, ):
        self.name = name
        self.initializer = initializer
    def accept(self, visitor : Visitor):
        visitor.visit_variable_declaration(self)

class Variable(Expr):
    def __init__(self, name : Token, ):
        self.name = name
    def accept(self, visitor : Visitor):
        visitor.visit_variable(self)

class Literal(Expr):
    def __init__(self, name : Token, parameters : List[Token], body : Expr, ):
        self.name = name
        self.parameters = parameters
        self.body = body
    def accept(self, visitor : Visitor):
        visitor.visit_literal(self)

class Grouping(Expr):
    def __init__(self, paren : Token, enclosed : Expr, ):
        self.paren = paren
        self.enclosed = enclosed
    def accept(self, visitor : Visitor):
        visitor.visit_grouping(self)

class Flow(Expr):
    def __init__(self, keyword : Token, enclosed : Expr, ):
        self.keyword = keyword
        self.enclosed = enclosed
    def accept(self, visitor : Visitor):
        visitor.visit_flow(self)


