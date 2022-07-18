import lib.getWindowProperty as getWindowProperty
import GRAMMAR as GRAMMAR
def getListOfLines(data):
    return data.split("\n")
def getLengthOfList(data):
    return len(data)

def lexer(lines):
    wp=getWindowProperty.getWindowPropertyLexer(lines, GRAMMAR.SYNTAX.DEFINE_WINDOW_PROPERTY)
    wpLength=getLengthOfList(wp)
    for i in range(wpLength):
        x=getWindowProperty.returnWindowPropertyAsHtml(wp[i], "hello world")
        print(x)