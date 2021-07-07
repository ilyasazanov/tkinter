import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.button = tk.Button(self, text='Append', command=self.on_click)
        self.button.pack()

        self.pack()

    def on_click(self):
        print('Hello World!')
        print(self.parent.__str__)
        print(self.parent.__dict__)