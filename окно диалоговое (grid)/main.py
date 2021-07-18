from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Диалоговое окно в Tkinter")
        self.pack(fill=BOTH, expand=True)

        # Добавлено небольшое пространство между виджетами в сетке.
        # Параметр weight создает возможность расширения второго столбца и четвертого ряда.
        # В этом ряду и столбце находится текстовой виджет,
        # поэтому текстовое поле при расширении окна заполняет все свомодное место.
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        # Метка создается и помещается в сетку.
        # Если не указываются строка и столбец, тогда она занимает первую строку и столбец сетки (row=0, column=0).
        # Метка закрепляется у западной (левой) стотоны окна sticky=W
        # и имеет определенные отступы вокруг своих границ.
        lbl = Label(self, text="Окна")
        lbl.grid(sticky=W, pady=4, padx=5)

        # Создается текстовый виджет и помещается во второй ряд и первый столбец (row=1, column=0).
        # И охватывает два столбца и четыре строки (columnspan=2, rowspan=4).
        # Между виджетом и левым краем корневого окна присутствует пространство в 4 пикселя (padx=4).
        # Также, виджет закреплен около всех четырех сторон (sticky=E + W + S + N).
        # Поэтому, когда окно расширяется, виджеты текстов увеличиваются во всех направлениях.
        area = Text(self)
        #area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=4, sticky=E + W + S + N)
        area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=4, sticky='nwse')

        # Эти две кнопки находятся возле текстового виджета.
        abtn = Button(self, text="Активир.")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Закрыть")
        cbtn.grid(row=2, column=3, pady=4)

        # Эти две кнопки находятся под текстовым виджетом.
        # Кнопка «Помощь» расположена в первом столбце,
        # а кнопка «Готово» в последнем столбце.
        hbtn = Button(self, text="Помощь")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="Готово")
        obtn.grid(row=5, column=3)


def main():
    root = Tk()
    root.geometry("350x300+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()