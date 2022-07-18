import lib.getWindowProperty as getWindowProperty
import GRAMMAR as GRAMMAR
def getListOfLines(data):
    return data.split("\n")
def getLengthOfList(data):
    return len(data)

def lexer(lines):
    wp=getWindowProperty.getWindowPropertyLexer(lines, GRAMMAR.SYNTAX.DEFINE_WINDOW_PROPERTY)
    wpLength=getLengthOfList(wp)
    cIfWp = 0
    for type in wp[0]:
            x = getWindowProperty.returnWindowPropertyAsHtml(type, wp[1][cIfWp])
            print(x)
            cIfWp += 1
            
            
