import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from funk import solving_eq


def main():
    label_res_x_1.config(text="")
    label_res_x_2.config(text="")
    label_res.config(text="")

    a = float(entry_a.get() or 0)
    b = float(entry_b.get() or 0)
    c = float(entry_c.get() or 0)

    try:
        answer = solving_eq(a, b, c)

    except ValueError:
        messagebox.showerror("Error", "Неверный формат ввода")

    if len(answer) == 1:
        label_res.config(text=answer[0])

    elif len(answer) == 2:
        label_res.config(text=answer[0])
        label_res_x_1.config(text=answer[1])

    elif len(answer) == 3:
        label_res.config(text=answer[0])
        label_res_x_1.config(text=answer[1])
        label_res_x_2.config(text=answer[2])

    x = np.linspace(-10, 10, 400)
    eq = a * x**2 + b * x + c
    plt.plot(x, eq)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Визуализация функции")
    plt.grid(True)
    plt.show()


def clean_window():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    label_res_x_1.config(text="")
    label_res_x_2.config(text="")
    label_res.config(text="")


window = tk.Tk()
window.title("Решение квадратных уравнений")

label_1 = tk.Label(window, text="Введите коэффициенты квадратного уравнения:")
label_1.grid(row=0, column=0, columnspan=7, padx=5, pady=5)
entry_a = tk.Entry(window, width=5)
entry_a.grid(row=1, column=0, padx=5, pady=5)
entry_a.insert(0, "0")
label_x2 = tk.Label(window, text="x² + ")
label_x2.grid(row=1, column=1, padx=5, pady=5)
entry_b = tk.Entry(window, width=5)
entry_b.grid(row=1, column=2, padx=5, pady=5)
entry_b.insert(0, "0")
label_x = tk.Label(window, text="x + ")
label_x.grid(row=1, column=3, padx=5, pady=5)
entry_c = tk.Entry(window, width=5)
entry_c.insert(0, "0")
entry_c.grid(row=1, column=4, padx=5, pady=5)
label_0 = tk.Label(window, text="= 0")
label_0.grid(row=1, column=5, padx=5, pady=5)

label_res = tk.Label(window)
label_res.grid(row=3, column=0, columnspan=7, padx=5, pady=5)
label_res_x_1 = tk.Label(window)
label_res_x_1.grid(row=4, column=0, columnspan=7, padx=5, pady=5)
label_res_x_2 = tk.Label(window)
label_res_x_2.grid(row=5, column=0, columnspan=7, padx=5, pady=5)

solving = tk.Button(window, text="Решить", command=main)
solving.grid(row=2, column=0, padx=5, pady=5)
clear = tk.Button(window, text="Очистить", command=clean_window)
clear.grid(row=2, column=1, padx=5, pady=5)

window.mainloop()
