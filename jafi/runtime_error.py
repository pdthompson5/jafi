class RuntimeError(Exception):
    def __init__(self, line : int, message: str, *args: object) -> None:
        self.message = message
        self.line = line