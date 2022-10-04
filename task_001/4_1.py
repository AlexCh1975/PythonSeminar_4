# Задайте строку из набора чисел. Напишите программу, которая покажет большее
# и меньшее число. В качестве разделителя используйте пробел.

# in 11 23 90 -8 12 7 45 -44
# out -44 90

# in 1, 6. 8: 9! -4
# out -4 9

# in 1 y 6 г 8
# out 'The data is incorrect'

# in 7ц 5ч 7
# out 'The data is incorrect'

def check(line):
    arr = line.split()
    for i in arr:
        # if not i.replace('-', '').isdigit():
        if not i.strip('-').isdigit():
           return [] 
    return arr

def min_max(array):
    if array:
        return min(array, key = int), max(array, key = int)
    return []

array = check(input("Список: "))
print(*array)
print(*min_max(array))