import openai

class DallEContext:
    def __init__(self, apiKey: str):
        self.APIKey = apiKey

    def Initialize(self) -> bool:
        openai.api_key = self.APIKey
        
        return True

    def Prompt(self, message: str, dimensions: str):
        return openai.Image.create(prompt=message, n=1, size=dimensions)
 

    


