# Напишите корни квадратного уравнения Ax**2 + Bx +C = 0,
# с помощью модуля. Запросите значения A, B, C 3 раза.
# Уравнения и корни запишите в файл.

# Enter the coefficient 'a': 1        1x ** 2 + 2x + 3
# Enter the coefficient 'b': 2        The first root: 1.00    
# Enter the coefficient 'c': -3       The first root: -3.00
#                                     5x ** 2 + 6x + -7 
# Enter the coefficient 'a': 5        The first root: 0.73
# Enter the coefficient 'b': 6        The first root: -1.93
# Enter the coefficient 'c': -7       8x ** 2 + 9x + -10
#                                     The first root: 0.69
# Enter the coefficient 'a': 8        The first root: -1.81
# Enter the coefficient 'b': 9 
# Enter the coefficient 'c': -10 

from encodings import utf_8
from math import sqrt

def quadratic_equation(a, b, c):

    discriminant = b ** 2 - 4 * a * c
    with open("task_002/out.txt", 'a', encoding='utf_8') as data:
        data.write(f"{a}x^2 + {b}x + {c} = 0\n")
        if discriminant > 0 and a:
            data.write(str((-b + sqrt(discriminant) )/ (2 * a)) + "\n")
            data.write(str((-b - sqrt(discriminant) )/ (2 * a)) + "\n")
            # return x1, x2
        elif discriminant == 0 and b:
            data.write(str(-(b / (2 * a))) + "\n")
            # return x1
        else:
            data.write("Действительных корней нет!\n")
            # return []

# res  = quadratic_equation(1, 2, -3)
# quadratic_equation(5, 6, -7)
# quadratic_equation(1, 2, -3)
# quadratic_equation(8, 9, -10)


# for i in range(3):
#     quadratic_equation(int(input()), int(input()), int(input()))
quadratic_equation(int(input()), int(input()), int(input()))