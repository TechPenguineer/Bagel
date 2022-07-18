import lib.getWindowProperty as getWindowProperty
import GRAMMAR as GRAMMAR
def getListOfLines(data):
    return data.split("\n")

def lexer(lines):
    wp=getWindowProperty.getWindowPropertyLexer(lines, GRAMMAR.SYNTAX.DEFINE_WINDOW_PROPERTY)
    x=getWindowProperty.returnWindowPropertyAsHtml(wp[0], "hello world")
    print(x)