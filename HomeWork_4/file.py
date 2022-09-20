            # 1. Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# num = float(input('Введите число: '))
# d =  int(input("Введите число заданной точности после запятой: "))
# print(round(num, d))

            # 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# n = int(input("Введите число: "))
# list = []
# d = 2
# m = n # Запомним исходное число
# while d * d <= n:
#         if n % d == 0:
#             list.append(d)
#             n//=d
#         else:
#             d += 1
# list.append(n) # Добавим последнеё простое число
# print('{} = {}' .format(m, list)) # Выводим исходное число и все простые множители.

            # 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

            # 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from calendar import c
import os
os.system("cls")
from random import randint
import itertools

k = int(input('Задайте натуральную степень k: '))

ratio_list = list([randint(0, 101) for i in range(k+1)]) # задаем случайный список
if ratio_list[0] == 0: # если будет равен 0, томногочлен может быть неверным
    ratio_list[0] = randint(1, 101)
print(ratio_list)

def get_polynomial(k, ratio_list): # далее идет загугливание информации
    str1 = ['*x**']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratio_list, str1, range(k, 1, -1), fillvalue = '') if a !=0]
    # с помощью этого метода мы объединяем несколько списков в список кортежей с самой длинной итерацией
    # пустые кортежи заполняем пустотой ('')
    print(polynomial)
    for x in polynomial:
        x.append(' + ') # проставляем + между кортежами
    polynomial = list(itertools.chain(*polynomial)) # объединяем в один список
    print(polynomial)
    polynomial[-1] = ' = 0' # добавляем концовочку (меняем последний '+' на '= 0')
    return "".join(map(str, polynomial)).replace(' 1*x',' x') # возвращаем строку

list = get_polynomial(k, ratio_list)
print(list)

with open('33_Polynomial.txt', 'w') as data:
    data.write(list)


# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
