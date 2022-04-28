
# What do I need this class to do:
# Open file, read contents, scanner -> parser -> interpreter 

import logging
import sys

from scanner import Scanner
from jafi_parser import Parser
from ast_printer import AST_Printer
from interpreter import Interpreter



    


class Jafi:

    def __init__(self, log_level):
        self.log_level = log_level
        self.interpreter = Interpreter()

    def read_file(self, filename: str) -> str:
        try:
            jafi_file = open(filename)
            return jafi_file.read()
        except Exception as e:
            print("Could not find jafi file " + filename + ".")
            sys.exit(65)


    def run_file(self, filename: str):
        file_contents = self.read_file(filename)
        scanner = Scanner(file_contents, self.log_level)
        tokens = scanner.scan()

        for token in tokens:
            print(token)

        parser = Parser(tokens, self.log_level)
        expressions = parser.parse()
        
        # printer = AST_Printer()
        # for expr in expressions:
        #     print(printer.print(expr))

        for expr in expressions:
            print(self.interpreter.evaluate(expr))
        


        


if __name__ == "__main__":
    if len(sys.argv) == 2:
        log_map = {
            "debug": logging.DEBUG,
            "info": logging.INFO,
            "critical" : logging.CRITICAL,
            "error" : logging.ERROR
        }
        try:
            level = log_map[sys.argv[1]]    
        except:
            level = logging.ERROR
        jafi = Jafi(level)
    else:
        jafi = Jafi(logging.ERROR)
    jafi.run_file("test.jafi")

    