from tkinter import *
from tkinter import messagebox
import pyperclip  # - pip install pyperclip
import pyshorteners  # - pip install pyshorteners

root = Tk()
root.title("Сокращение ссылок")
root.geometry("400x260")
root["bg"] = "#4E4A4A"

Label(root, text="Добро пожаловать в\nсократер ссылок!", font = "Calibri 15 bold", bg = "#4E4A4A", fg = "#FFFFFF").pack(pady=5)
Label(root, text="Введите ссылку:", font = "Calibri 11 bold", bg = "#4E4A4A", fg = "#FFFFFF").pack(pady=5)

link = Entry(root, width=40)
link.pack()

Label(root, text="Сокращённая ссылка:", font = "Calibri 11 bold", bg = "#4E4A4A", fg = "#FFFFFF").pack(pady=5)

res = Entry(root, width=40)
res.pack()


def copytoclipboard():
	url = res.get()
	pyperclip.copy(url)


def short():
	try:
		a = link.get()
		s = pyshorteners.Shortener().tinyurl.short(a)
		res.insert(0, s)
	except:
		messagebox.showerror("Сокращение ссылок", "Неверная ссылка!")

Button(root, text="Сократить", command=short).pack(pady=10)
Button(root, text="Скопировать", command=copytoclipboard).pack(pady=5)
root.mainloop()