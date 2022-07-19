def removeLineNumber(data):
    ret = []
    for x in data:
        a = str(x)
        new_data = a.split(" ")
        new_data.pop(0)
        ret.append(new_data)
    return ret

def makeString(s):
    str1 = ""
   
    # traverse in the string 
    for ele in s:
        str1 += " " + ele 
   
    # return string 
    return str1