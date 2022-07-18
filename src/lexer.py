import lib.getWindowProperty as getWindowProperty
import GRAMMAR as GRAMMAR
def getListOfLines(data):
    return data.split("\n")
def getLengthOfList(data):
    return len(data)

def lexer(lines):
    ret_data = """"""
    wp=getWindowProperty.getWindowPropertyLexer(lines, GRAMMAR.SYNTAX.DEFINE_WINDOW_PROPERTY)
    wpLength=getLengthOfList(wp)
    cIfWp = 0
    for type in wp[0]:
            x = getWindowProperty.returnWindowPropertyAsHtml(type, wp[1][cIfWp])
            
            cIfWp += 1
            
            
