

def removeWhitespaceFromReader(dataList):
    dataList = [i for i in dataList if i]
    return dataList

def acceptStringData(data):
   dataIndex = data.index("=")
   dataLength = len(data)
   startPos = dataLength - 1 - dataIndex 
   res = []
   cI=0
   for i in range(startPos):
        res.append(data[i+startPos+1])
   final = " ".join(res)
   return final

def getWindowPropertyLexer(lines, windowPropertyIndicator):

    # Finds Tokens in the lines
    tokens = []
    token_value = []
    lineNumb = 0
    tokensFound = 0
    for line in lines:
        lineNumb += 1
        cL = line.split(" ")
        onToken = 0
        tokensOnLine = [cL]
        #print(tokensOnLine)
        for token in cL:
            onToken += 1
            if token == windowPropertyIndicator:
                 tokensFound += 1
                 #print(cL)
                 # print( "Window Property Set on line: " + str(lineNumb) + ": Property of " + str(tokensOnLine[0][ onToken ] ) + " " + str(tokensFound))
                 if(cL[onToken+1]=="="):
                     token_value.append(acceptStringData(tokensOnLine[0]))
                 tokens.append(tokensOnLine[0][ onToken ])

    return [tokens, token_value]

def returnWindowPropertyAsHtml(propertyType, value):
    if propertyType == "title":
        return "<title>" + value + "</title>"
    if propertyType == "ico":
        return "<link rel='icon' href='" + value + "'>"