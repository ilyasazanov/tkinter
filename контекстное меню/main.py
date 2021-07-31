import tkinter as tk

class AddPopupMenu:
    def copy_selection(self):
        try:
            selection_text = self.selection_get()
        except tk.TclError:
            return

        root.clipboard_clear()
        root.clipboard_append(selection_text)
        print('Copied:', selection_text)

    def delete_selection(self):
        try:
            self.delete('sel.first', 'sel.last')
        except tk.TclError:
            pass  # Nothing selected

    def cut_selection(self):
        self.copy_selection()
        self.delete_selection()

    def paste_from_clipboard(self):
        try:
            clipboard_text = root.clipboard_get()
        except tk.TclError:
            pass
        else:
            self.delete_selection()
            self.insert(tk.INSERT, clipboard_text)

    def select_all(self):
        # Пример отсюда https://stackoverflow.com/a/13808423/4752653
        self.tag_add(tk.SEL, "1.0", tk.END)
        self.mark_set(tk.INSERT, "1.0")
        self.see(tk.INSERT)

    def show_context_menu(self, event):
        pos_x = self.winfo_rootx() + event.x
        pos_y = self.winfo_rooty() + event.y
        self.popup_menu.tk_popup(pos_x, pos_y)

    def init_menu(self):
        menu = tk.Menu(self, tearoff=False)
        menu.add_command(label="Вырезать", command=self.cut_selection)
        menu.add_command(label="Копировать", command=self.copy_selection)
        menu.add_command(label="Вставить", command=self.paste_from_clipboard)
        menu.add_command(label="Удалить", command=self.delete_selection)
        menu.add_separator()
        menu.add_command(label="Выделить все", command=self.select_all)
        return menu

    def __init__(self, widget_class, *args, **kwargs):
        widget_class.__init__(self, *args, **kwargs)
        self.popup_menu = self.init_menu()
        self.bind("<3>", self.show_context_menu)


class MyText(tk.Text, AddPopupMenu):
    def __init__(self, *args, **kwargs):
        AddPopupMenu.__init__(self, tk.Text, *args, **kwargs)


class MyEntry(tk.Entry, AddPopupMenu):
    def __init__(self, *args, **kwargs):
        AddPopupMenu.__init__(self, tk.Entry, *args, **kwargs)


root = tk.Tk()

text1 = MyText(root, width=50, height=10)
text1.pack()

text2 = MyText(root, width=50, height=10)
text2.pack()

entry1 = MyEntry(root, width=50)
entry1.pack()

entry2 = MyEntry(root, width=50)
entry2.pack()

root.mainloop()