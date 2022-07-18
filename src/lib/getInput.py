import lib.COLOR as COLOR

def startShell():
    command = input(COLOR.COLOR_PREFABS.BOLD_COLOR + COLOR.COLORS.CYAN + "--> " + COLOR.COLOR_PREFABS.END_COLOR)
    argv = list(command.split(" "))
    return argv