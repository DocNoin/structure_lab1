import tkinter as tk
from tkinter import messagebox

def printset(a):
    return "Элементы: " + str(a) + "\nКоличество: " + str(len(a))

def handle_click():
    text = entry_input.get()
    if text == "":
        messagebox.showwarning("Ошибка", "Вы ничего не ввели")
        return
    a = []
    b = 'ТУФХтуфх1234'
    for i in text:
        if i in b:
            a.append(i)
    label_result.config(text=printset(set(a)))

window = tk.Tk()
window.title("Лабораторная работа: множества")
window.geometry("400x300")

label_input = tk.Label(window, text='Введите цифры и русские буквы:')
label_input.pack()

entry_input = tk.Entry(window, width=40)
entry_input.pack()

button = tk.Button(window, text = 'Постороить и вывести множество', command=handle_click)
button.pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()
