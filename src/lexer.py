import lib.getWindowProperty as getWindowProperty
import lib.commentLine  as commentLine
import GRAMMAR as GRAMMAR
import lib.sortLineNumber as sortLineNumber
import lib.formatToFileType as formatToFileType
import lib.textProperty as textProperty
def getListOfLines(data):
    return data.split("\n")
def getLengthOfList(data):
    return len(data)

def lexer(lines):
    ret_data = []
    ret = []


    # Defines window properties
    wp=getWindowProperty.getWindowPropertyLexer(lines, GRAMMAR.SYNTAX.DEFINE_WINDOW_PROPERTY)
    cIfWp = 0
    for type in wp[0]:
            x = getWindowProperty.returnWindowPropertyAsHtml(wp[2][cIfWp], type, wp[1][cIfWp])
            ret_data.append(x)
            cIfWp += 1


    # Defines comment lines
    cl=commentLine.addCommentLineLexer(lines, GRAMMAR.SYNTAX.DEFINE_COMMENT_LINE)
    cIfCl = 0
    for type in cl[0]:
        x = commentLine.returnCommentAsHtml(cl[1][cIfCl], type)
        ret_data.append(x)
        cIfCl += 1


    # Defines text properties
    tp=textProperty.addTextBlock(lines, GRAMMAR.SYNTAX.DEFINE_TEXT_BLOCK_START)
    cIfTp = 0
    for type in tp[0]:
        #x = textProperty.returnTextBlocktAsHtml(cl[1][cIfCl], type)
        print(tp)
        #ret_data.append(x)
        cIfTp += 1


    # Sorts the line numbers
    sl=sortLineNumber.sortLineNumbers(ret_data)


    # Formats the lines
    sl=formatToFileType.removeLineNumber(sl)
    cI = 0
    for ele in sl:
        x = formatToFileType.makeString(sl[cI])
        cI += 1
        ret.append(x)
    return ret
    