
from .error_reporting import report_error
from .jafi_token import Token, TokenType

import logging


class Scanner:
    def __init__(self, source: str, log_level):
        logging.basicConfig()
        logging.getLogger("Scanner").setLevel(log_level)  
        self.logger = logging.getLogger("Scanner")   


        self.source = source
        self.current = 0
        self.line = 1
        self.tokens = []
        self.keywords = {
            "False" : TokenType.FALSE,
            "True" : TokenType.TRUE,
            "None" : TokenType.NONE,
            "if" : TokenType.IF,
            "then" : TokenType.THEN,
            "else" : TokenType.ELSE,
            "def" : TokenType.DEF,
            "set" : TokenType.SET,
            "flow" : TokenType.FLOW,
            "num" : TokenType.NUMBER_TYPE,
            "str" : TokenType.STRING_TYPE,
            "bool" : TokenType.BOOL_TYPE,
            # "list" : TokenType.LIST_TYPE,
            # "dict" : TokenType.DICT_TYPE,
            # "tuple" : TokenType.TUPLE_TYPE
        }

    def scan(self):
        while not self.is_at_end():
            self.scan_token()
        self.add_token(("", TokenType.EOF))
        return self.tokens

    def scan_token(self):
        current_char = self.advance()
        self.logger.debug("Scanning character " + current_char)
        token_map = {
            "(" : TokenType.LEFT_PAREN,
            ")" : TokenType.RIGHT_PAREN,
            "{" : TokenType.LEFT_BRACE,
            "}" : TokenType.RIGHT_BRACE,
            "," : TokenType.COMMA,
            ";" : TokenType.SEMICOLON,
            ":" : TokenType.COLON,
            "=" : TokenType.EQUAL,
            "`" : TokenType.TICK,
            "\\" : TokenType.LAMBDA,
        }


        try:
            type_fetched = token_map[current_char]
        except:
            if current_char == "#": self.comment()
            elif current_char == " ": pass
            elif current_char == "\t": pass
            elif current_char == "\r": pass
            elif current_char == "\n": self.line += 1
            elif current_char == "\'": self.char()
            elif current_char == '"' : self.string()
            # negative numbers or minus function
            elif current_char == "-" : 
                if self.is_digit(self.peek()): self.number("0", negative=True)
                else: self.identifier(current_char)
            elif self.is_digit(current_char): self.number(current_char)
            else: self.identifier(current_char)

            return
            
        
        type_tuple = (current_char, type_fetched)

        self.add_token(type_tuple)



    def add_token(self, args):
        lexeme = args[0]
        type = args[1]
        if len(args) == 2:
            literal = None
        else:
            literal = args[2]

        self.tokens.append(Token(lexeme, type, literal, self.line))


    def is_at_end(self) -> bool:
        return len(self.source) == self.current

    def peek(self) -> str:
        return self.source[self.current]

    def peek_next(self) -> str:
        return self.source[self.current+1]

    def advance(self) -> str:
        character = self.source[self.current]
        self.current += 1
        return character

    def is_digit(self, a):
        return a in {str(x) for x in range(0, 10)}
    
    def number(self, digit: str, negative = False):
        while not self.is_at_end() and self.peek() != "." and self.is_digit(self.peek()):
            digit += self.advance()

        if not self.is_at_end() and self.peek() == ".":
            digit += self.advance()
            while not self.is_at_end() and self.is_digit(self.peek()):
                digit += self.advance()       

        digit_as_int = float(digit)

        if negative:
            digit_as_int = -digit_as_int

        self.add_token((digit, TokenType.NUMBER, digit_as_int))

    def char(self):
        character = ""
        if not self.is_at_end() and self.peek() != "'":
            character += self.advance()
        if self.is_at_end() or self.peek() != "\'":
            report_error("Unterminated Character", self.line)
            return
        self.advance() #consume closing "'"

        self.add_token((character, TokenType.CHAR, character))

    def string(self):
        string = ""
        while not self.is_at_end() and self.peek() != '"':
            if(self.peek() == '\n'): self.line += 1
            string += self.advance()
        if self.is_at_end():
            report_error("Unterminated String", self.line)
            return
        self.advance() #consume closing '"'"

        self.add_token((string, TokenType.STRING, list(string)))

    def identifier(self, name: str):
        # read in name until whitespace
        while not self.is_at_end() and not self.peek().isspace() and self.is_allowable_char_in_name():
            name += self.advance()
        
        if name in self.keywords.keys():
            if name == "False":
                self.add_token((name, self.keywords[name], False))
            elif name == "True":
                self.add_token((name, self.keywords[name], True))
            else:
                self.add_token((name, self.keywords[name]))
        else:
            self.add_token((name, TokenType.IDENTIFIER))

    def is_allowable_char_in_name(self) -> bool:
        return not self.peek() in ["(", ")", ",", ":"]


    def comment(self):
        while not self.is_at_end() and self.peek() != "\n":
            self.advance()