import lib.getWindowProperty as getWindowProperty
import lib.commentLine  as commentLine
import GRAMMAR as GRAMMAR
import lib.sortLineNumber as sortLineNumber
import lib.formatToFileType as formatToFileType
def getListOfLines(data):
    return data.split("\n")
def getLengthOfList(data):
    return len(data)

def lexer(lines):
    ret_data = []

    # Defines window properties
    wp=getWindowProperty.getWindowPropertyLexer(lines, GRAMMAR.SYNTAX.DEFINE_WINDOW_PROPERTY)
    wpLength=getLengthOfList(wp)
    cIfWp = 0
    for type in wp[0]:
            x = getWindowProperty.returnWindowPropertyAsHtml(wp[2][cIfWp], type, wp[1][cIfWp])
            ret_data.append(x)
            cIfWp += 1
        

    # Defines comment lines
    cl=commentLine.addCommentLineLexer(lines, GRAMMAR.SYNTAX.DEFINE_COMMENT_LINE)
    clLength=getLengthOfList(cl)
    cIfCl = 0
    for type in cl[0]:
        x = commentLine.returnCommentAsHtml(cl[1][cIfCl], type)
        ret_data.append(x)
        cIfCl += 1


    # Sorts the line numbers
    sl=sortLineNumber.sortLineNumbers(ret_data)
    # Formats the lines
    sl=formatToFileType.removeLineNumber(sl)
    

    return sl
    