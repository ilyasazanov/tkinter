# https://www.youtube.com/watch?v=vt3obgYnj4E

from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry('300x500')
root.title('Войдите в систему')


def registration():
    lbl_label = Label(text='Для входа в систему- авторизуйтесь!')
    lbl_login = Label(text='Введите логин:')
    ent_login = Entry()

    lbl_pass1 = Label(text='Введите пароль:')
    ent_pass1 = Entry()

    lbl_pass2 = Label(text='Подтвердите пароль:')
    ent_pass2 = Entry(show='*')

    btn_register = Button(text='Зарегистрироваться', command=lambda: save())

    lbl_label.pack()
    lbl_login.pack()
    ent_login.pack()
    lbl_pass1.pack()
    ent_pass1.pack()
    lbl_pass2.pack()
    ent_pass2.pack()
    btn_register.pack()

    def save():
        # Асоциативный массив (словарь)
        login_pass_save = {}
        # Ключ=логин, значение=пароль
        login_pass_save[ent_login.get()] = ent_pass1.get()

        f = open('logins.txt', 'wb')
        # Сохраняем
        pickle.dump(login_pass_save, f)
        f.close()

        # И открываем окно авторизации
        login()


def login():
    lbl_label = Label(text='Войдите в систему')
    lbl_login = Label(text='Введите логин:')
    ent_login = Entry()

    lbl_pass = Label(text='Введите пароль:')
    ent_pass = Entry(show='*')

    btn_register = Button(text='Войти', command=lambda: check_log_pass())

    lbl_label.pack()
    lbl_login.pack()
    ent_login.pack()
    lbl_pass.pack()
    ent_pass.pack()
    btn_register.pack()

    def check_log_pass():
        f = open('logins.txt', 'rb')
        a = pickle.load(f)
        f.close()

        # Если есть логин
        if ent_login.get() in a:
            if ent_pass.get() == a[ent_login.get()]:
                messagebox.showinfo('Вход выполнен', 'Привет')
            else:
                messagebox.showerror('Ошибка', 'неверный пароль')
        else:
            messagebox.showerror('Ошибка', 'неверный логин')


registration()

root.mainloop()

