def writeToFileOnLine(fileName, data):
    for x in data:
        with open(fileName, 'a') as file:
            file.write(str(x) + "\n")



