import tkinter


def mainWindow1(*w, **kw):
    root = tkinter.Tk()
    root.title('window 1')

    def butCallback():
        root.destroy()
        mainWindow2()

    but1 = tkinter.Button(root,
                          text="-> window 2",
                          command=butCallback)
    but1.pack()
    root.mainloop()


def mainWindow2(*w, **kw):
    root = tkinter.Tk()
    root.title('window 2')

    def butCallback():
        root.destroy()
        mainWindow1()


mainWindow1()