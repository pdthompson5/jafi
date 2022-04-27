
from abc import ABC, abstractmethod
from expr import *
def Visitor(ABC):
    @abstractmethod
    def visit_function_declaration(expr: FunctionDeclaration):
        pass

    @abstractmethod
    def visit_variable_declaration(expr: VariableDeclaration):
        pass

    @abstractmethod
    def visit_variable(expr: Variable):
        pass

    @abstractmethod
    def visit_literal(expr: Literal):
        pass

    @abstractmethod
    def visit_grouping(expr: Grouping):
        pass

    @abstractmethod
    def visit_flow(expr: Flow):
        pass

    @abstractmethod
    def visit_function_call(expr: FunctionCall):
        pass

