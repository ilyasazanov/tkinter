from tkinter import *

root = Tk()

# отзывчивая рамка для конкретных ячеек
#root.grid_rowconfigure(0, weight=1)
#root.grid_columnconfigure(0, weight=1)
# или оня же в циклах для всех ячеек
n_rows =2
n_columns =3
for i in range(n_rows):
    root.grid_rowconfigure(i,  weight=1)
for i in range(n_columns):
    root.grid_columnconfigure(i,  weight=1)

# создание виджетов согласно рамки 3х4
Label(text="Имя:").grid(row=0, column=0,
                        sticky=W,
                        pady=10, padx=10)
table_name = Entry()
table_name.grid(row=0, column=1,
                columnspan=3,
                sticky=W + E, padx=10)

Label(text="Столбцов:").grid(
    row=1, column=0, sticky=W,
    padx=10, pady=10)
Spinbox(width=7, from_=1, to=50) \
    .grid(row=1, column=1, padx=10)
Label(text="Строк:") \
    .grid(row=1, column=2, sticky=E)
Spinbox(width=7, from_=1, to=100) \
    .grid(row=1, column=3, sticky=E, padx=10)

Button(text="Справка") \
    .grid(row=2, column=0, pady=10, padx=10)
Button(text="Вставить") \
    .grid(row=2, column=2)
Button(text="Отменить") \
    .grid(row=2, column=3, padx=10)

root.mainloop()