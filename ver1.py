import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from funk import solving_eq
import re
import sqlite3


def parse_eq(eq):
    try:
        m = re.match(
            r"\s*([+-]?\d*\.?\d*)\s*x\^2\s*([+-]?\d*\.?\d*)\s*x\s*([+-]?\d*\.?\d*)\s*$",
            eq,
        )
        if m:
            a = float(m.group(1).replace(" ", "") or "1")
            b = float(m.group(2).replace(" ", "") or "1")
            c = float(m.group(3).replace(" ", "") or "0")
            return [a, b, c]

        raise ValueError("Неверный формат ввода")

    except ValueError:
        messagebox.showerror("Error", "Неверный формат ввода")


def main():
    global canvas_widget
    label_res_x_1.config(text="")
    label_res_x_2.config(text="")
    label_res.config(text="")

    eq = entry_eq.get()
    abc = parse_eq(eq)
    a = abc[0]
    b = abc[1]
    c = abc[2]
    answer = solving_eq(a, b, c)
    try:
        canvas_widget.destroy()
    except:
        pass
    visual_eq(a, b, c)

    if len(answer) == 1:
        label_res.config(text=answer[0])

    elif len(answer) == 2:
        label_res.config(text=answer[0])
        label_res_x_1.config(text=answer[1])

    elif len(answer) == 3:
        label_res.config(text=answer[0])
        label_res_x_1.config(text=answer[1])
        label_res_x_2.config(text=answer[2])


def visual_eq(a, b, c):
    global canvas_widget
    x = np.linspace(-10, 10, 400)
    eq = a * x**2 + b * x + c
    fig, axes = plt.subplots()
    axes.plot(x, eq)
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    axes.set_title("Визуализация")
    axes.grid(True)
    axes.axhline(0, color="black", lw=1)
    axes.axvline(0, color="black", lw=1)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=6, column=0, columnspan=7, padx=5, pady=5)


def clean_window():
    global canvas_widget
    entry_eq.delete(0, tk.END)
    entry_eq.insert(0, "0x^2+0x+0")
    label_res_x_1.config(text="")
    label_res_x_2.config(text="")
    label_res.config(text="")
    try:
        canvas_widget.destroy()
    except:
        pass

def history_bd():
    global window_h
    eqs = []
    window_h = tk.Tk()
    window_h.title("История запросов")
    window_h.geometry("250x200")

    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute(""" SELECT * from request_history""")
        hist = cursor.fetchall()
        
        for row in hist:
            st = str(row[1]) + "x^2"
            if row[2] < 0:
                st += str(row[2]) + "x"
            else:
                st += "+" + str(row[2]) + "x"
            if row[2] < 0:
                st += str(row[3])
            else:
                st += "+" + str(row[3])
            eqs.append(st)

        b = tk.Button(window_h, text="Очистить историю", command=clean_history)
        b.grid(row=0, column=0, padx=5, pady=5)
        listbox = tk.Listbox(window_h)
        listbox.grid(row=1, column=0, columnspan=2, sticky=tk.EW, padx=5, pady=20)

        for s in eqs:
            listbox.insert(tk.END, s)
        listbox.bind("<Double-1>", again)


def clean_history():
    window_h.destroy()
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute(""" DELETE FROM request_history""")
        clean_window()


def again(event):
    global canvas_widget
    select_item = event.widget.curselection()
    if select_item:
        i = int(select_item[0])
        item = event.widget.get(i)
    entry_eq.delete(0, tk.END)
    entry_eq.insert(0, item)
    label_res_x_1.config(text="")
    label_res_x_2.config(text="")
    label_res.config(text="")
    try:
        canvas_widget.destroy()
    except:
        pass
    main()


window = tk.Tk()
window.title("Решение квадратных уравнений")

label_1 = tk.Label(window, text="Введите квадратное уравнение:")
label_1.grid(row=0, column=0, columnspan=7, padx=5, pady=5)
entry_eq = tk.Entry(window, width=30)
entry_eq.grid(row=2, column=0, columnspan=5, padx=5, pady=5)
entry_eq.insert(0, "0x^2+0x+0")
label_0 = tk.Label(window, text="= 0")
label_0.grid(row=2, column=6, padx=5, pady=5)

label_res = tk.Label(window)
label_res.grid(row=5, column=0, columnspan=7, padx=5, pady=5)
label_res_x_1 = tk.Label(window)
label_res_x_1.grid(row=6, column=0, columnspan=7, padx=5, pady=5)
label_res_x_2 = tk.Label(window)
label_res_x_2.grid(row=7, column=0, columnspan=7, padx=5, pady=5)

solving = tk.Button(window, text="Решить", command=main)
solving.grid(row=4, column=0, padx=5, pady=5)
clear = tk.Button(window, text="Очистить", command=clean_window)
clear.grid(row=4, column=1, padx=5, pady=5)
history = tk.Button(window, text="История", command=history_bd)
history.grid(row=4, column=2, padx=5, pady=5)




window.mainloop()
