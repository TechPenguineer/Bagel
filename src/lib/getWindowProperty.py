def getWindowPropertyLexer(lines, windowPropertyIndicator):

    # Finds Tokens in the lines
    lineNumb = 0
    for line in lines:
        lineNumb += 1
        cL = line.split(" ")
        for token in cL:
            if token == windowPropertyIndicator:
                print( "Window Property Set on line: " + str(lineNumb))