import tkinter as tk
from tkinter import messagebox

def printset(a):
    sorted_elements = sorted(list(a)) 

    elements_str = ", ".join(sorted_elements) if sorted_elements else "нет подходящих"
    
    return "Элементы: " + elements_str + '. ' + "Количество: " + str(len(a)) + '.'


def zad_1():
    text = entry_input.get()
    if text == "":
        messagebox.showwarning("Ошибка!", "Вы ничего не ввели.")
        return
    
    a = set() 
    for i in text:
        if ('T' <= i <= 'X') or ('t' <= i <= 'x') or ('1' <= i <= '4'):
            a.add(i)
            
    label_result.config(text=printset(a))


def zad_2():
    text1 = entry_str1.get()
    text2 = entry_str2.get()

    if text1 == "" or text2 == "":
        messagebox.showwarning("Ошибка!", "Обе строки должны быть заполнены.")
        return

    str1 = set(text1)
    str2 = set(text2)
    
    if str1.issubset(str2):
        result = "Все символы первой строки входят во вторую!"
    elif str2.issubset(str1):
        result = "Все символы второй строки входят в первую!" 
    else: 
        result = "Ни одна строка не содержит все символы другой"   
    result_text = result + "\n" + "\n" +"Строка №1 " + "\n" +  printset(str1) + "\n" + "\n" + "Строка №2 " + "\n" +  printset(str2) 
    label_compare_result.config(text=result_text)   


window = tk.Tk()
window.title("Семенова вмо22")
window.geometry("700x410")
window.configure(bg="#EDF3BA")

label_input = tk.Label(window, text='Введите цифры и русские буквы:', fg="#791111", font=("Verdana", 15, "bold"), bg="#EDF3BA")
label_input.pack()

entry_input = tk.Entry(window, width=100)
entry_input.pack()

button = tk.Button(window, text = 'Постороить и вывести множество', command=zad_1, fg="#791111", font=("Verdana", 13))
button.pack()

label_result = tk.Label(window, text="", font=("Verdana", 13), bg="#EDF3BA")
label_result.pack()

label_str1 = tk.Label(window, text='Введите текст', fg="#791111", font=("Verdana", 15, "bold"), bg="#EDF3BA")
label_str1.pack()

entry_str1 = tk.Entry(window, width=100)
entry_str1.pack()

label_str2 = tk.Label(window, text='Введите текст', fg="#791111", font=("Verdana", 15, "bold"), bg="#EDF3BA")
label_str2.pack()

entry_str2 = tk.Entry(window, width=100)
entry_str2.pack()

button_compare = tk.Button(window, text='Узнать, содержатся ли все символы одной строки в другой', command=zad_2, fg="#791111", font=("Verdana", 13))
button_compare.pack()

label_compare_result = tk.Label(window, text="", font=("Verdana", 13), bg="#EDF3BA", width=200)
label_compare_result.pack()


window.mainloop()
