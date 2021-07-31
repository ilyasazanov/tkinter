import tkinter as tk


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        # задаем контекстное меню через встроенные события
        self.menu = tk.Menu(tearoff=0)
        self.menu.add_command(label="Вырезать", accelerator="Ctrl+X", command=lambda: self.w.focus_force() or self.w.event_generate("<<Cut>>"))
        self.menu.add_command(label="Копировать", accelerator="Ctrl+С", command=lambda: self.w.focus_force() or self.w.event_generate("<<Copy>>"))
        self.menu.add_command(label="Вставить", accelerator="Ctrl+V", command=lambda: self.w.focus_force() or self.w.event_generate("<<Paste>>"))
        self.menu.add_command(label="Удалить", accelerator="Delete", command=lambda: self.w.focus_force() or self.w.event_generate("<<Clear>>"))
        self.menu.add_separator()
        self.menu.add_command(label="Выделить все", accelerator="Ctrl+A", command=lambda: self.w.focus_force() or self.w.event_generate("<<SelectAll>>"))

        # создаем текстовые поля
        entry_1 = tk.Entry()
        entry_1.pack()

        entry_2 = tk.Entry()
        entry_2.pack()

        entry_3 = tk.Entry()
        entry_3.pack()

        # создаем многострочный текст
        text = tk.Text()
        text.pack()
        # вешаем меню на многострочный текст
        text.bind("<Button-3>", self.func)
        # вешаем меню на тестовые поля через класс
        self.bind_class("Entry", "<Button-3><ButtonRelease-3>", self.func)

    def func(self, event):
        self.menu.post(event.x_root, event.y_root)
        self.w = event.widget


if __name__ == "__main__":
    main = Main()
    main.mainloop()