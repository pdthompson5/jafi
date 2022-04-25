



from jafi_token import Token
from jafi_token import TokenType 
from typing import List
from expr import *
from error_reporting import report_error_token


class Parser:
    def __init__(self, tokens: List[Token]):
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

        self.function_declaration()

    def function_declaration(self):
        if self.match(TokenType.DEF):
            name = self.advance()
            
            self.consume(TokenType.LEFT_PAREN, "Expect '(' after function name")
            parameters = []
            
            while self.peek() != TokenType.RIGHT_PAREN:
                
                parameters.append(self.advance())
                if not self.match(TokenType.COMMA):
                    break

            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after parameter list")

            for para  in parameters:
                print(para)
            
            self.consume(TokenType.LEFT_BRACE, "Expect '{' after function declaration")
            # body = self.expression()
            body = Literal(Token("", TokenType.STRING, "", 25))
            self.consume(TokenType.RIGHT_BRACE, "Expect '}' after function definition")

            return FunctionDeclaration(name, parameters, body)
            

        else:
            return self.flow()
    
    def flow(self):
        pass



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
    
    def consume(self, type: TokenType, message : str):
        if type == self.peek().type:
            self.advance()
        else:
            report_error_token(self.peek(), message)
            self.advance()
            raise Exception()
