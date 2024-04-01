import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from funk import solving_eq
import re


def parse_eq(eq):
    try:
        m = re.match(
            r"\s*([+-]?\d*\.?\d*)\s*x\^2\s*([+-]?\d*\.?\d*)\s*x\s*([+-]?\d*\.?\d*)\s*$",
            eq,
        )
        if m:
            a = float(m.group(1) or "1")
            b = float(m.group(2) or "1")
            c = float(m.group(3))
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
    if len(answer) == 3:
        min_edge = answer[2][0][0] - 10
        max_edge = answer[2][0][0] + 10
        roots = [answer[2][0][0]]
    elif len(answer) == 4:
        min_edge = min(answer[3][0][0], answer[3][1][0]) - 2
        max_edge = max(answer[3][0][0], answer[3][1][0]) + 2
        roots = [answer[3][0][0], answer[3][1][0]]
    elif a == 0:
        min_edge = -10
        max_edge = 10
        roots = []
    else:
        min_edge = -b / (2 * a) - 10
        max_edge = -b / (2 * a) + 10
        roots = []
    visual_eq(a, b, c, min_edge, max_edge, roots)

    if len(answer) == 1:
        label_res.config(text=answer[0])

    elif len(answer) == 3:
        label_res.config(text=answer[0])
        label_res_x_1.config(text=answer[1])

    elif len(answer) == 4:
        label_res.config(text=answer[0])
        label_res_x_1.config(text=answer[1])
        label_res_x_2.config(text=answer[2])


def visual_eq(a, b, c, left, right, roots):
    global canvas_widget
    x = np.linspace(left, right, 400)
    eq = a * x**2 + b * x + c
    fig, axes = plt.subplots()
    axes.plot(x, eq)
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    axes.set_title("Визуализация")
    axes.grid(True)
    axes.axhline(0, color="black", lw=1)
    axes.axvline(0, color="black", lw=1)
    axes.autoscale_view()
    axes.scatter(roots, np.zeros_like(roots), color="red", label="Roots")
    for root in roots:
        axes.annotate(
            f"({root:.2f}, 0)",
            xy=(root, 0),
            xytext=(root, -10),
            textcoords="offset points",
            ha="center",
            va="top",
            bbox=dict(boxstyle="round,pad=0.5", fc="red", alpha=0.5),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
        )
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=8, column=0, columnspan=7, padx=5, pady=5)


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


window = tk.Tk()
window.title("Решение квадратных уравнений")

label_title = tk.Label(window, text="Введите квадратное уравнение:")
label_title.grid(row=0, column=0, columnspan=7, padx=5, pady=5)
label_format = tk.Label(window, text="(Формат ввода: ax^2+bx+c)")
label_format.grid(row=1, column=0, columnspan=7, padx=5, pady=5)
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

window.mainloop()
