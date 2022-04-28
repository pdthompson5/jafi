

from jafi_token import Token, TokenType


def map(arguments, interpreter):
    function = arguments[0]

    new_list = []
    for element in arguments[1]:
        #TODO: Determine what to pass for token 
        new_list.append(function.call([element], interpreter, Token("", TokenType.NONE, None, -1)))

    return new_list