import sys
import logging
from typing import List

from .scanner import Scanner
from .jafi_parser import Parser
from .ast_printer import AST_Printer
from .interpreter import Interpreter, stringify, to_jafi, to_python
from .runtime_error import RuntimeError

from .expr import FunctionCall, Variable, Literal
from .jafi_token import Token, TokenType



class Jafi:

    def __init__(self, log_level=logging.ERROR, debug=False):
        self.log_level = log_level
        self.interpreter = Interpreter()
        self.debug = debug

    def read_file(self, filename: str) -> str:
        try:
            jafi_file = open(filename)
            return jafi_file.read()
        except Exception as e:
            print("Could not find jafi file " + filename + ".")
            sys.exit(65)

    def call_function(self, function_name: str, *args):
        name = Token(function_name, TokenType.IDENTIFIER, None, -1)
        l_value = Variable(name)
        
        tokenized_arguments = [Literal(to_jafi(argument)) for argument in args]

        #TODO: Convert back into python value 
            # Function go to string, char arrays go to Strings, numbers with trailing zeroes go to int
        return to_python(self.interpreter.evaluate(FunctionCall(name, l_value, tokenized_arguments)))



    def run_file(self, filename: str):
        file_contents = self.read_file(filename)
        jafi_scanner = Scanner(file_contents, self.log_level)
        tokens = jafi_scanner.scan()

        # for token in tokens:
        #     print(token)

        parser = Parser(tokens, self.log_level)
        expressions = parser.parse()

        if(parser.had_error):
            sys.exit(65)
        
        # printer = AST_Printer()
        # for expr in expressions:
        #     print(printer.print(expr))

        eval = None
        for expr in expressions:
            try:
                eval = self.interpreter.evaluate(expr)
                if self.debug:
                    print(stringify(eval))
            except RuntimeError:
                sys.exit(70)
        return to_python(eval)