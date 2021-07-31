# https://www.delftstack.com/ru/howto/python-tkinter/how-to-bind-enter-key-to-a-function-in-tkinter/

import tkinter as tk


class app(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.label = tk.Label(self.root, text="")
        self.label.pack()
        self.root.bind('<Return>', self.callback)
        self.root.mainloop()

    def callback(self, event):

        # Мы поместили атрибут keysym объекта event в показанную метку.
        # keysym является ключевым символом события клавиатуры. Enter - это Return, как мы ввели выше.
        self.label["text"] = "You pressed {}".format(event.keysym)


app()