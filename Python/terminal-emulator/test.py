# import os
# print(os.name)
# if os.name == 'nt':
#     import win32api
#     import win32con


# def file_is_hidden(p):
#     if os.name == 'nt':
#         attribute = win32api.GetFileAttributes(p)
#         return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
#     else:
#         return p.startswith('.')  # linux-osx


# file_list = [f for f in os.listdir('.') if not file_is_hidden(f)]
# print(file_list)


def multi(*args):
    print(*args)
    for i in args:
        print(i)

args = ["ls","ll","-a"]

if __name__ == "__main__":
    print(*args[1:])
else:
    print("not a module")