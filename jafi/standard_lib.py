

from jafi_token import Token, TokenType


def map(arguments, interpreter):
    function = arguments[0]

    new_list = []
    for element in arguments[1]:
        #TODO: Determine what to pass for token 
        new_list.append(function.call([element], interpreter, Token("", TokenType.NONE, None, -1)))

    return new_list

def filter(arguments, interpreter):
    function = arguments[0]

    new_list = []
    for element in arguments[1]:
        if function.call([element], interpreter, Token("", TokenType.NONE, None, -1)):
            new_list.append(element)
    
    return new_list

def reduce(arguments, interpreter):
    start_value = arguments[0]
    function = arguments[1]

    for element in arguments[2]:
        start_value = function.call([start_value, element], interpreter, Token("", TokenType.NONE, None, -1))

    return start_value

def cons(arguments, interpreter):
    return "Not implemented"