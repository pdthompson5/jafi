
from abc import ABC, abstractmethod
from expr import *
class Visitor(ABC):
    @abstractmethod
    def visit_function_declaration(self, expr: FunctionDeclaration):
        pass

    @abstractmethod
    def visit_variable_declaration(self, expr: VariableDeclaration):
        pass

    @abstractmethod
    def visit_variable(self, expr: Variable):
        pass

    @abstractmethod
    def visit_literal(self, expr: Literal):
        pass

    @abstractmethod
    def visit_grouping(self, expr: Grouping):
        pass

    @abstractmethod
    def visit_flow(self, expr: Flow):
        pass

    @abstractmethod
    def visit_function_call(self, expr: FunctionCall):
        pass

