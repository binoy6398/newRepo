import os
from Command import Command


def execute():
    path = os.getcwd()
    return path


pwd = Command("pwd", "Show current directory path", execute)
