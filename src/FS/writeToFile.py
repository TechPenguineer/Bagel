def writeToFileOnLine(fileName, data, onLine=0):
    with open(fileName, 'r') as file:
        data = file.readlines()
    line = onLine-1
    data[line] = 'Mage\n'
    with open(fileName, 'w') as file:
        file.writelines( data ) 



