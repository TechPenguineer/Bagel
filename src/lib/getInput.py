import lib.COLOR as COLOR

def startShell():
    command = input("--> ")
    argv = list(command.split(" "))
    print("\n\n")
    return argv