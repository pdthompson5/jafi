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

    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()

    FALSE = auto()
    TRUE = auto()
    NONE = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    DEF = auto()
    SET = auto()
    FLOW = auto()
    EOF = auto()

    # New keywords for static typing 
    NUMBER_TYPE = auto()
    STRING_TYPE = auto()
    BOOL_TYPE = auto()
    LIST_TYPE = auto()
    DICT_TYPE = auto()
    TUPLE_TYPE = auto()
    
class Token:
    def __init__(self, lexeme: str, type: TokenType, literal: object, line: int) -> None:
        self.lexeme = lexeme
        self.type = type
        self.literal = literal
        self.line = line

    def __str__(self):
        return f"Type: {self.type} Lexeme: '{self.lexeme}' Literal: {self.literal} Line: {self.line}"




