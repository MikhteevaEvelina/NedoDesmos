import math


def solving_eq(a, b, c):
    
    D = b**2 - 4 * a * c
    if a == 0 and b == 0 and c == 0:
        return ["Решением данного уравнения является вся числовая прямая"]
              
    elif D < 0 or a == 0 and b == 0:
        return ["Уравнение не имеет решений в действительных числах"]
    
    elif a == 0:
        x = -c / b
        if x == -0.0:
            x = 0.0
        return ["Уравнение имеет единственное решение", "x = " + str(x)]

    elif D == 0:
        x = -b / (2 * a)
        if x == -0.0:
            x = 0.0
        return ["Уравнение имеет единственное решение", "x = " + str(x)]
        
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        if x1 == -0.0:
            x1 = 0.0
        if x2 == -0.0:
            x2 = 0.0
        return ["Уравнение имеет два решения", "x1 = " + str(x1), "x2 = " + str(x2)]