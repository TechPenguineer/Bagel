
# arg0  arg1   arg2
# bagel build <file>
# if ends with .bagl then build
def build(argv):
    index=0
    for arg in argv:
        print(arg  + " " + str(index))
        index+=1