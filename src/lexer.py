import lib.getWindowProperty as getWindowProperty
import GRAMMAR as GRAMMAR
def getListOfLines(data):
    return data.split("\n")

def lexer(lines):
    getWindowProperty.getWindowPropertyLexer(lines, GRAMMAR.SYNTAX.DEFINE_WINDOW_PROPERTY)
