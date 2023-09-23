import os
import sys
from DallE import DallEContext

def Main():
    context = DallEContext(os.environ["OPENAI_KEY"])

    context.Initialize()
    print(context.Prompt(sys.argv[1], sys.argv[2]))

    return

Main()