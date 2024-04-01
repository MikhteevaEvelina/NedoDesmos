import math
import sqlite3
id = 0

def solving_eq(a, b, c, d=0, e=0): # ax^2 + bx + c = dx + e
    global id
    id += 1

    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute(""" INSERT INTO request_history (id, a, b, c, d, e) VALUES (?, ?, ?, ?, ?, ?); """, (id, a, b, c, d, e))


    D = (b - d)**2 - 4 * a * (c -e)
    if a == 0 and b - d == 0 and c - e == 0:
        return ["Решением данного уравнения является вся числовая прямая"]

    elif a == 0 and b - d == 0:
        return ["Уравнение не имеет решений"]

    elif D < 0:
        return ["Уравнение не имеет решений в действительных числах"]

    else:
        answer = roots(a, b, c, D, d, e)
        if len(answer) == 1:
            return ["Уравнение имеет единственное решение", "x = " + str(answer[0][0])]

        elif len(answer) == 2:
            return ["Уравнение имеет два решения", "x1 = " + str(answer[0][0]), "x2 = " + str(answer[1][0])]
        


def roots(a, b, c, D, d=0, e=0):

    if a == 0:
        x = -(c-e) / (b - d)
        y = d * x + e
        if x == -0.0:
            x = 0.0
        if y == -0.0:
            y == 0.0
        return [(x, y)]

    elif D == 0:
        x = -(b - d) / (2 * a)
        y = d * x + e
        if x == -0.0:
            x = 0.0
        if y == -0.0:
            y == 0.0
        return [(x, y)]

    else:
        x1 = (-(b - d) + math.sqrt(D)) / (2 * a)
        x2 = (-(b - d) - math.sqrt(D)) / (2 * a)
        y1 = d * x1 + e
        y2 = d * x2 + e
        if x1 == -0.0:
            x1 = 0.0
        if x2 == -0.0:
            x2 = 0.0
        if y1 == -0.0:
            y1 = 0.0
        if y2 == -0.0:
            y2 = 0.0
        return [(x1, y1), (x2, y2)]
