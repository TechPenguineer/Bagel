import os
import lexer as bagelLexer
import lib.getInput as getInput
# The Bagel language is a simple language that is used to create an advanced, stylistic, and reactive web pages.
dir = "/__tests__/webpage.bagl"
cwd = os.getcwd()

def getContent(path):
 with open(path, 'r') as f:
   return f.read()


argv = getInput.startShell()
# print(argv)

if(argv[0] == "bagel"):
    if(argv[1] == "build"):
      if(argv[2]!=None):
        data = getContent(argv[2])
        lOl = bagelLexer.getListOfLines(data)
        bagelLexer.lexer(lOl)    
      else:
        print("Unknown command")
