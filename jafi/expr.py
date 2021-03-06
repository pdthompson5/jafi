
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

class LambdaExpr(Expr):
    def __init__(self, name : Token, parameters : List[Token], body : Expr, ):
        self.name = name
        self.parameters = parameters
        self.body = body
    def accept(self, visitor):
        return visitor.visit_lambda_expr(self)

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

class FunctionCall(Expr):
    def __init__(self, paren : Token, l_value : Expr, arguments : List[Expr], ):
        self.paren = paren
        self.l_value = l_value
        self.arguments = arguments
    def accept(self, visitor):
        return visitor.visit_function_call(self)

class IfExpr(Expr):
    def __init__(self, keyword : Token, condition : Expr, if_true : Expr, else_clause : Expr, ):
        self.keyword = keyword
        self.condition = condition
        self.if_true = if_true
        self.else_clause = else_clause
    def accept(self, visitor):
        return visitor.visit_if_expr(self)

