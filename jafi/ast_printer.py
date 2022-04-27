from expr import *
from visitor import Visitor


class AST_Printer(Visitor):
    def print(self, expr: Expr) -> str:
        return expr.accept(self)
    
    def visit_function_declaration(self, expr: FunctionDeclaration):
        param_string = "("
        for param in expr.parameters:
            param_string += param + ","
        param_string += ")"

        return self.parenthesize(f"def {expr.name.lexeme} {param_string}", expr.body)
    
    def visit_variable_declaration(self, expr: VariableDeclaration):
        return self.parenthesize("set", expr.initializer)

    
    def visit_variable(self, expr: Variable):
        return expr.name.lexeme

    
    def visit_literal(self, expr: Literal):
        return expr.literal.__str__()

    
    def visit_grouping(self, expr: Grouping):
        return self.parenthesize("group", [expr.enclosed])

    
    def visit_flow(self, expr: Flow):
        return self.parenthesize("flow", [expr.starting_val] + expr.body)
    
    def visit_function_call(self, expr: FunctionCall):
        return self.parenthesize("", [expr.l_value] + expr.arguments)



    def parenthesize(self, name: str, exprs: List[Expr]) -> str:
        string = f"({name}"
        for expr in exprs:
            string += " "
            string += expr.accept(self)
        string +=")"

        return string



def test_printer():
    printer = AST_Printer()
    exprs = []
    exprs.append(Literal(15))
    for expr in exprs:
        print(printer.print(expr))
    pass