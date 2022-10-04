# Задайте два числа. Напишите должна находить НОК (наименьшее общее кратное) 
# этих двух чисел.

# in 17 11          in 14 18          in 0 0
# out 187           out 126           out 0

from math import gcd

a = int(input())
b = int(input())

print(a * b // gcd(a, b))
