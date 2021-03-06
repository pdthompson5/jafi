from enum import Enum, auto

class TokenType(Enum):
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    SEMICOLON = auto()
    COLON = auto()
    EQUAL = auto()
    TICK = auto()
    LAMBDA = auto()

    IDENTIFIER = auto()
    STRING = auto()
    CHAR = auto()
    NUMBER = auto()

    FALSE = auto()
    TRUE = auto()
    NONE = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    DEF = auto()
    SET = auto()
    EOF = auto()
    
class Token:
    def __init__(self, lexeme: str, type: TokenType, literal: object, line: int) -> None:
        self.lexeme = lexeme
        self.type = type
        self.literal = literal
        self.line = line

    def __str__(self):
        return f"Type: {self.type} Lexeme: '{self.lexeme}' Literal: {self.literal} Line: {self.line}"




