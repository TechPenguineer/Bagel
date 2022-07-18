import os
import lexer as bagelLexer

dir = "/__tests__/webpage.bagl"
cwd = os.getcwd()
def getContent(path):
 with open(cwd + path, 'r') as f:
   return f.read()

data = getContent(dir)

lOl = bagelLexer.getListOfLines(data)
bagelLexer.lexer(lOl)