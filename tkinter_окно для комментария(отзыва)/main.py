from tkinter import Tk, Text, BOTH, X, N, LEFT, RAISED
from tkinter.ttk import Frame, Label, Entry, Style


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Оставить отзыв")
        self.style = Style()
        self.style.theme_use("default")

        # Первая рамка является базовой. На ней располагаются все остальные рамки
        self.pack(fill=BOTH, expand=True)

        # Первые два виджета размещены на первой рамке.
        # Поле для ввода данных растянуто горизонтально с параметрами fill и expand.
        # Добавлена граница для понимания расположения рамок
        frame1 = Frame(self, relief=RAISED, borderwidth=1)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Заголовок", width=10)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self, relief=RAISED, borderwidth=1)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Автор", width=10)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        # В третьей рамке мы разместили ярлык и виджет для ввода текста.
        # Ярлык закреплен по северной стороне anchor=N,
        # а виджет текста занимает все остальное пространство.
        frame3 = Frame(self, relief=RAISED, borderwidth=1)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Отзыв", width=10)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)


def main():
    root = Tk()
    root.geometry("300x300+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()