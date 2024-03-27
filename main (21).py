#coding:utf-8
#Задача 27
array1 = [int(x) for x in input("Введите первый массив из 17 элементов через пробел:").split()]
array2 = [int(x) for x in input("Введите второй массив из 25 элементов:").split()]
array3 = list(set(array1 + array2))
print("Третий массив из уникальных элементов:")
print(array3)

#Задача 28
import random
m = 5
n = 4
b = [[random.randint(0, 5) for _ in range(n)] for _ in range(m)]
print("Матрица b: ")
for row in b:
    print(row)
non_zero_count = sum([1 for row in b for element in row if element != 0])
print("Количество ненулевых элементов в матрице b: ", non_zero_count)
