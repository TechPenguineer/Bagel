

def removeWhitespaceFromReader(dataList):
    dataList = [i for i in dataList if i]
    return dataList

def acceptStringData(data):
    # = : 3   tL : 11         
    dataIndex = data.index("=")
    current_pos = 0
    startPos = dataIndex+1
    ret = []
    for ele in data:
        current_pos += 1
        if current_pos == startPos:
            for x in range(len(data)-startPos):
                ret.append(data[current_pos+x])
    retdata = ' '.join(ret)  
    #print(retdata)        
    return retdata

   # dataLength = len(data)
   # startPos = dataLength - 1 - dataIndex 
   # res = []
   # cI=0
   # for i in range(startPos):
   #      res.append(data[i+startPos])
   # final = " ".join(res)
   # return final

def getWindowPropertyLexer(lines, windowPropertyIndicator):

    # Finds Tokens in the lines
    tokens = []
    token_value = []
    lineNumb=[]
    lineNumber = 0
    tokensFound = 0
    for line in lines:
        lineNumber += 1
        cL = line.split(" ")
        onToken = 0
        tokensOnLine = [cL]
        #print(tokensOnLine)
        for token in cL:
            onToken += 1
            if token == windowPropertyIndicator:
                 equals_token_loc = 0
                 tokensFound += 1
                 #print(cL)
                 #print( "Window Property Set on line: " + str(lineNumb) + ": Property of " + str(tokensOnLine[0][ onToken ] ) + " " + str(tokensFound))
                 if(cL[onToken+1]=="="):
                     token_value.append(acceptStringData(tokensOnLine[0]))
                 tokens.append(tokensOnLine[0][ onToken ])
                 lineNumb.append(lineNumber)
    
    return [tokens, token_value, lineNumb]

def returnWindowPropertyAsHtml(lineNumb, propertyType, value):
    expected_property_types = ["title", "ico", "responsive"]
    if propertyType == "title":
        return  str(lineNumb) + " <title>" + value + "</title>"
    if propertyType == "ico":
        return str(lineNumb) + " <link rel='icon' href='" + value + "'>"
    if propertyType == "responsive":
        if(value == "scaling"):
            return str(lineNumb) + " <meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        else:
            return str(lineNumb) + " <meta name='viewport' content='" + value + "'>"
    if propertyType not in expected_property_types:
        print("Unknown Window Property Type: " + propertyType)