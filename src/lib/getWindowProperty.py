

def removeWhitespaceFromReader(dataList):
    dataList = [i for i in dataList if i]
    return dataList

def acceptStringData(dataList):
    quotes = '"'
    dataList.split(quotes)

class WINDOW_LEXER_CONST:
    ...
def getWindowPropertyLexer(lines, windowPropertyIndicator):

    # Finds Tokens in the lines
    tokens = []
    lineNumb = 0
    tokensFound = 0
    for line in lines:
        lineNumb += 1
        cL = line.split(" ")
        onToken = 0
        tokensOnLine = [removeWhitespaceFromReader(cL)]
        #print(tokensOnLine)
        for token in cL:
            onToken += 1
            if token == windowPropertyIndicator:
                 tokensFound += 1
                 print( "Window Property Set on line: " + str(lineNumb) + ": Property of " + str(tokensOnLine[0][ onToken ] ) + " " + str(tokensFound))
                 tokens.append(tokensOnLine[0][ onToken ])
    return tokens

def returnWindowPropertyAsHtml(propertyType, value):
    if propertyType == "title":
        return "<title>" + value + "</title>"
    if propertyType == "ico":
        return "<link rel='icon' href='" + value + "'>"