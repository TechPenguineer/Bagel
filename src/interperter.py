import lib.COLOR as COLOR
import lib.build as build
LINEBUG= COLOR.COLOR_PREFABS.BOLD_COLOR + COLOR.COLORS.CYAN + "--> "

command = input(LINEBUG + COLOR.COLORS.END)
argv = list(command.split(" "))

print (argv)
build.build(argv[1])


print(COLOR.COLOR_PREFABS.END_COLOR)