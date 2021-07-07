import tkinter as tk


class LeftFrame(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.l_text = tk.Text(self.parent, width = 40, height = 10)
        self.l_text.grid(row=0, column=0)
        self.l_text.bind("<Key>", self.return_data)

    def return_data(self, event):
        data = self.l_text.get(1.0, tk.END)
        # uses the variable name "app" assigned to the main window class.
        # then calls a method inside that class to append the data from another class text box
        app.add_to_right_frame(data)


class RightFrame(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.r_text = tk.Text(self.parent, width = 40, height = 10)
        self.r_text.grid(row=0, column=1)
        self.r_text.bind("<Key>", self.return_data)

        print( self.parent.__str__ )
        #print(self.parent.__dict__)
        print( self.__str__ )

    def return_data(self, event):
        data = self.r_text.get(1.0, tk.END)
        # uses the variable name "app" assigned to the main window class.
        # then calls a method inside that class to append the data from another class text box
        app.add_to_left_frame(data)


class MainWindow(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.master = root
        self.main_frame = tk.Frame(self.master)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        #makes a class attribute of each frame so it can be manipulated later
        self.f1 = LeftFrame(self.main_frame)
        self.f2 = RightFrame(self.main_frame)

    def add_to_left_frame(self, data):
        self.f1.l_text.delete(1.0, tk.END)
        self.f1.l_text.insert(1.0, data)

    def add_to_right_frame(self, data):
        self.f2.r_text.delete(1.0, tk.END)
        self.f2.r_text.insert(1.0, data)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()