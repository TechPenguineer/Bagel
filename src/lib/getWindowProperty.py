def removeWhitespaceFromReader(dataList):
    return ' '.join(dataList).split()

def getWindowPropertyLexer(lines, windowPropertyIndicator):

    # Finds Tokens in the lines
    lineNumb = 0
    for line in lines:
        lineNumb += 1
        cL = line.split(" ")
        onToken = 0
        tokensOnLine = [removeWhitespaceFromReader(cL)]
        #print(tokensOnLine)
        for token in cL:
           onToken += 1
           if token == windowPropertyIndicator:
                 propertyToken = onToken
                 print( "Window Property Set on line: " + str(lineNumb) + ": Property of " + str(tokensOnLine[0][ onToken ] ))