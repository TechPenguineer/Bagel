

def removeWhitespaceFromReader(dataList):
    dataList = [i for i in dataList if i]
    return dataList

def getAfterIndicator(data, commentLength, commentStart):
   startPos = commentStart
   # print("startPos: " + str(startPos))
   line_len = len(data)
   ret=[]
   for i in range(line_len):
        #print(i)
        if i != startPos:
            pass 
        else:
            for a in range(commentLength):
                #print(a)
                ret.append(data[i+a])
   return " ".join(ret)
    



def addCommentLineLexer(lines, defineCommnetIndicator):

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
        lineLength = len(cL)
        res=[]
        cI = 0
        comment_length=0
        #print(tokensOnLine)
        for token in cL:
            onToken += 1
            if token == defineCommnetIndicator:
                 tokensFound += 1
                 # print( "Comment line on line: " + str(lineNumb) + "\nStarting On Token " + str(onToken) + "\nEnding on token: " + str(lineLength))
                 #print('lineLength: ' + str(lineLength-onToken))
                 token_value.append( getAfterIndicator(cL, lineLength-onToken, onToken) )
    return token_value

def returnCommentAsHtml(value):
    return "<!-- " + value + " -->"