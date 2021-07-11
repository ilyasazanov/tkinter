import tkinter as tk

# Создается новое окно с заголовком "Введите домашний адрес"
window = tk.Tk()
window.title("Введите домашний адрес")

# Создается новая рамка `frm_form` для ярлыков с текстом и
# Однострочных полей для ввода информации об адресе.
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Помещает рамку в окно приложения.
frm_form.pack()

# Создает ярлык и текстовок поле для ввода имени.
lbl_first_name = tk.Label(master=frm_form, text="Имя:")
ent_first_name = tk.Entry(master=frm_form, width=50)
# Использует менеджер геометрии grid для размещения ярлыка и
# однострочного поля для ввода текста в первый и второй столбец
# первой строки сетки.
lbl_first_name.grid(row=0, column=0, sticky="e")
ent_first_name.grid(row=0, column=1)

# Создает ярлык и текстовок поле для ввода фамилии.
lbl_last_name = tk.Label(master=frm_form, text="Фамилия:")
ent_last_name = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на вторую строку сетки
lbl_last_name.grid(row=1, column=0, sticky="e")
ent_last_name.grid(row=1, column=1)

# Создает ярлык и текстовок поле для ввода первого адреса.
lbl_address1 = tk.Label(master=frm_form, text="Адрес 1:")
ent_address1 = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на третьей строке сетки.
lbl_address1.grid(row=2, column=0, sticky="e")
ent_address1.grid(row=2, column=1)

# Создает ярлык и текстовок поле для ввода второго адреса.
lbl_address2 = tk.Label(master=frm_form, text="Адрес 2:")
ent_address2 = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на четвертой строке сетки.
lbl_address2.grid(row=3, column=0, sticky=tk.E)
ent_address2.grid(row=3, column=1)

# Создает ярлык и текстовок поле для ввода города.
lbl_city = tk.Label(master=frm_form, text="Город:")
ent_city = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на пятой строке сетки.
lbl_city.grid(row=4, column=0, sticky=tk.E)
ent_city.grid(row=4, column=1)

# Создает ярлык и текстовок поле для ввода региона.
lbl_state = tk.Label(master=frm_form, text="Регион:")
ent_state = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на шестой строке сетки.
lbl_state.grid(row=5, column=0, sticky=tk.E)
ent_state.grid(row=5, column=1)

# Создает ярлык и текстовок поле для ввода почтового индекса
lbl_postal_code = tk.Label(master=frm_form, text="Почтовый индекс:")
ent_postal_code = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на седьмой строке сетки.
lbl_postal_code.grid(row=6, column=0, sticky=tk.E)
ent_postal_code.grid(row=6, column=1)

# Создает ярлык и текстовок поле для ввода страны.
lbl_country = tk.Label(master=frm_form, text="Страна:")
ent_country = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на восьмой строке сетки.
lbl_country.grid(row=7, column=0, sticky=tk.E)
ent_country.grid(row=7, column=1)

# Создает новую рамку `frm_buttons` для размещения
# кнопок "Отправить" и "Очистить". Данная рамка заполняет
# все окно в горизонтальном направлении с
# отступами в 5 пикселей горизонтально и вертикально.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Создает кнопку "Отправить" и размещает ее
# справа от рамки `frm_buttons`.
btn_submit = tk.Button(master=frm_buttons, text="Отправить")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Создает кнопку "Очистить" и размещает ее
# справа от рамки `frm_buttons`.
btn_clear = tk.Button(master=frm_buttons, text="Очистить")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

# Запуск приложения.
window.mainloop()