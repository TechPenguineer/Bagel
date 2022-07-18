import os
import lexer as bagelLexer
# The Bagel language is a simple language that is used to create an advanced, stylistic, and reactive web pages.
dir = "/__tests__/webpage.bagl"
cwd = os.getcwd()
def getContent(path):
 with open(cwd + path, 'r') as f:
   return f.read()

data = getContent(dir)

lOl = bagelLexer.getListOfLines(data)
bagelLexer.lexer(lOl)