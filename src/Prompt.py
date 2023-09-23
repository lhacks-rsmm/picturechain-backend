class Prompt:
    def __init__(self, _promptID: str, message: str, result: str):
        self.promptID = _promptID
        self.message = message
        self.result = result

    def toDict(self) -> dict:
        return dict({
            "id": self.promptID,
            "message": self.message,
            "result": self.result
        })