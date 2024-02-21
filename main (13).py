#coding: utf-8
#Задача 1
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    maximus = a
    minimus = b
else:
    maximus = b
    minimus = a
print("Ответ:")
print("Максимальное число:",maximus)
print("Минимальное чичсло:",minimus)

#Задча 2
a = int(input("Введите сторону квадрата: "))
b = int(input("Введите радиус круга: "))
if 2*b <= a:
    print("Круг впишется в квадрат")
else:
    print("Круг не впишется в квадрат")
    
#Задача 3
a = int(input("Введите число: "))
if a > 0:
    b = 1/a*a
else:
    b = a*a
print(b)

#Задача 4
a = int(input("Введите сторону квадрата: "))
b = int(input("Введите радиус круга: "))
if 2*b >= a:
    print("Квадрат впишется в круг")
else:
    print("Квадрат не впишется в круг")
    
#Задача 5
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print("Наибольшее число:", a)
elif b > a:
    print("Наибольшее число:", b)
else:
    print("Числа равны")
    
#Задача 6
a = int(input("Введите число: "))
if a<=0:
    b = a*a
else:
    b = 1/a*a
print(b)




