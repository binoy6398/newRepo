import tkinter as tk


class Terminal(tk.Text):

    def __init__(self, commands, master=None, **kw):
        self.commands = commands
        tk.Text.__init__(self, master, **kw)
        self.insert('1.0', '>>> ')  # first prompt
        # create input mark
        self.mark_set('input', 'insert')
        self.mark_gravity('input', 'left')
        # create proxy

        self._orig = self._w + "_orig"

        self.tk.call("rename", self._w, self._orig)

        self.tk.createcommand(self._w, self._proxy)
        # binding to Enter key
        self.bind("<Return>", self.enter)

    def _proxy(self, *args):
        largs = list(args)

        if args[0] == 'insert':
            if self.compare('insert', '<', 'input'):
                # move insertion cursor to the editable part
                # you can change 'end' with 'input'
                self.mark_set('insert', 'end')
        elif args[0] == "delete":
            if self.compare(largs[1], '<', 'input'):
                if len(largs) == 2:
                    return  
                largs[1] = 'input'  # move deletion start at 'input'
        result = self.tk.call((self._orig,) + tuple(largs))
        return result

    def enter(self, event):
        # get the user input
        user_input = self.get('input', 'end')
        # convert the user inputs to a list
        args = user_input.split()

        if args:
            command_name = args[0]

            if command_name in self.commands:
                command = self.commands[command_name]
                # print(*args[1:])
                output = command.execute(*args[1:])
                print(output)
                if output:
                    self.print_output(output)
            else:
                self.insert(
                    'end', '\ncommand not found')
        # display result and next promp
        self.insert(
            'end', '\n\n>>> ')
        # move input mark
        self.mark_set('input', 'insert')
        return "break"  # don't execute class method that inserts a newline

    def print_output(self, text):
        self.insert(
            'end', f'\n{text}')
