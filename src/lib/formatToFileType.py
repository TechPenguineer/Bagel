def removeLineNumber(data):
    ret = []
    for x in data:
        a = str(x)
        new_data = a.split(" ")
        new_data.pop(0)
        ret.append(new_data)
    return ret
