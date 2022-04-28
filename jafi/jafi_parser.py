



from ast import IfExp
from jafi_token import Token
from jafi_token import TokenType 
from typing import List
from expr import *
from error_reporting import report_error_token
import logging

# TODO: See if I can add infix operators into my grammar then just desugar them to functions 
class Parser:
    def __init__(self, tokens: List[Token], log_level):
        logging.basicConfig()
        logging.getLogger("Parser").setLevel(log_level)  
        self.logger = logging.getLogger("Parser")  

        self.tokens = tokens
        self.current = 0

    def parse(self) -> List[Expr]:
        expressions = []
        while not self.is_at_end():
            try:
                expressions.append(self.expression())
            except:
                return expressions
        return expressions

    def expression(self) -> Expr:
        return self.function_declaration()

    def function_declaration(self):
        if self.match(TokenType.DEF):
            self.logger.info("Matched function declaration")
            name = self.advance()
            
            self.consume(TokenType.LEFT_PAREN, "Expect '(' after function name")
            parameters = []
            
            while not self.check(TokenType.RIGHT_PAREN):
                parameters.append(self.advance())
                if not self.match(TokenType.COMMA):
                    break
            

            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after parameter list")

            
            self.consume(TokenType.LEFT_BRACE, "Expect '{' after function declaration")
            body = self.expression()
            self.consume(TokenType.RIGHT_BRACE, "Expect '}' after function definition")

            return FunctionDeclaration(name, parameters, body)
            

        else:
            return self.flow()
    
    def flow(self):
        if self.check(TokenType.FLOW):
            self.logger.info("Matched flow expression")
            keyword = self.advance()
            self.consume(TokenType.LEFT_PAREN, "Expect '(' after flow declaration")
            starting_val = self.expression()

            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after flow starting value")

            self.consume(TokenType.LEFT_BRACE, "Expect '{' after flow starting value")
            body = []
            while not self.check(TokenType.RIGHT_BRACE):
                body.append(self.expression())

            self.consume(TokenType.RIGHT_BRACE, "Expect '}' after flow body")

            return Flow(keyword, starting_val, body)
            
        else:
            return self.variable_declaration()


    def variable_declaration(self):
        if self.match(TokenType.SET):
            self.logger.info("Matched variable declaration")

            name = self.advance()
            self.consume(TokenType.EQUAL, "Expect '=' after variable name")
            initializer = self.expression()

            return VariableDeclaration(name, initializer)
        else:
            return self.if_expr()

    def if_expr(self):
        if self.check(TokenType.IF):
            keyword = self.advance()
            self.logger.info("Matched if expression")

            condition = self.expression()
            self.consume(TokenType.THEN, "Expect 'then' after if conditional.")

            if_true = self.expression()

            else_clause = Literal(None)
            if self.match(TokenType.ELSE):
                else_clause = self.expression()
            
            return IfExpr(keyword, condition, if_true, else_clause)
        else:
            return self.function_call()

# TODO: Check if you can use parenthesis inside of parameter lists -> You should be able to 

    def function_call(self):
        expr = self.variable()

        if self.check(TokenType.LEFT_PAREN):
            paren = self.advance()
            self.logger.info("Matched function call")
            arguments = []
            while not self.check(TokenType.RIGHT_PAREN):
                arguments.append(self.expression())
                if not self.match(TokenType.COMMA):
                    break
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after argument list")
            expr = FunctionCall(paren, expr, arguments)
            
        return expr


    def variable(self):
        if self.check(TokenType.IDENTIFIER):
            self.logger.info("Matched variable")
            name = self.advance()
            return Variable(name)
        else:
            return self.primary()

    def primary(self):
        if self.check_list([TokenType.TRUE, TokenType.FALSE, TokenType.STRING, TokenType.NUMBER, TokenType.NONE]):
            self.logger.info("Matched literal")
            return Literal(self.advance().literal)
        else:
            return self.grouping()
    
    def grouping(self):
        if self.check(TokenType.LEFT_PAREN):
            self.logger.info("Matched group")
            paren = self.advance()
            enclosed = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Unclosed Parenthesis")

            return Grouping(paren, enclosed)
        else:
            report_error_token(self.peek(), "Expect expression")
            return None 




    def advance(self) -> Token:
        token = self.tokens[self.current]
        self.current += 1
        return token

    def peek(self) -> Token:
        return self.tokens[self.current]

    def is_at_end(self) -> bool:
        return self.peek().type == TokenType.EOF

    def match(self, type: TokenType) -> bool:
        if type == self.peek().type:
            self.advance()
            return True 
        else:
            return False
    
    def check(self, type: TokenType) -> bool:
        return type == self.peek().type

    def check_list(self, types: List[TokenType]) -> bool:
        return self.peek().type in types 
    
    def consume(self, type: TokenType, message : str):
        if type == self.peek().type:
            self.advance()
        else:
            report_error_token(self.peek(), message)
            self.advance()
            raise Exception()
