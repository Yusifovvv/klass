#coding: utf-8

#Задание 1
p=int(input("Введите число"))
i = 2 ** 0.5
while  i < p:
    print(i)
    i = i + 1
    
#Задание 2
a = int(input("Введите число A"))
b = int(input("Введите число B"))
i = a + 1 
while i < b:
    print(i)
    i += 1 

#Задание 3
a = int(input("Введите число A"))
b = int(input("Введите число B"))
i = b - 1
while i > a:
    print(i)
    i -= 1
    
#Задание 4
n = int(input("Введите целое число N больше 1"))
k = 1
while 3 * k <= n:
    k += 1
    print(k)
    
#Задание 5
n = int(input("Введите целое число N больше 1"))
k = 1
while 3 * k > n:
    k += 1
    k -= 1 
    print(k)
    
#Задание 6
n = int(input("Введите натуральное число N: "))
i = 1 
while i < N:
    print(i)
    i += 1 


