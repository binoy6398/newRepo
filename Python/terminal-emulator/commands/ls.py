from Command import Command
import os


def execute(*args):
    for a in args:
        print("arg: ",a)
    dir_list = os.listdir()
    return "\n".join(dir_list)


ls = Command("ls", "Show files & folders in current directory", execute)
