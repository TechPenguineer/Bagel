
# arg0  arg1   arg2
# bagel build <file>
# if ends with .bagl then build
def build(argv):
    if argv[1].endswith(".bagl"):
        print("Building " + argv[1])
        return True
    else: 
        print(argv[2])
    