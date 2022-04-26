import tkinter as tk
from Terminal import Terminal
from commands import ls, pwd

commands = [ls, pwd]

commands_dict = {}

for cmd in commands:
    commands_dict[cmd.name] = cmd


root = tk.Tk()
root.title("Terminal")
tfield = Terminal(commands_dict, root, width=60, height=20, bg='black',
                  fg='white', insertbackground='white')
tfield.pack(fill=tk.BOTH, expand=1)
root.mainloop()
