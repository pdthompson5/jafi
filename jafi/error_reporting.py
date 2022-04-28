import sys
from jafi_token import Token

def report_error(message: str, line: int):
    print(f"[Jafi Error] {message} Line {line}", file=sys.stderr)

def report_error_token(token: Token, message: str):
    report_error(f"at '{token.lexeme}' {message}", token.line)
