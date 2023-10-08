# # Дан словарь, создать новый словарь поменяв местами ключ и значение.
#
# my_dict = {'key1': 15, 'key2': 'test', 'key3': '123'}
# print(my_dict)
#
# my_dict_2 = {
#     value: key
#     for key, value in my_dict.items()
# }
#
# print(my_dict_2)
#
#
# # Написать программу для нахождения факториала. Факториал натурального числа n
# # определяется как произведение всех натуральных чисел от 1 до n включительно.
# # реализацию выполняить в виде рекурсивной функции.
#
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         f = n * factorial(n - 1)
#         return f
#
#
# n = int(input('Введите число: '))
# print(factorial(n))
#
# ###########################################################################
#
# # Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать
# # для подсчета функцию.
#
# # Подсказка: для хранения данных использовать словарь.Для проверки
# # нахождения элемента в словаре использовать метод get(), либо оператор in
#
#
# num = '1 2 3 4 2 3 4 8 0 3 5 1 6 7 7 8 3 4 5'
# num_list = num.split()
#
# number = {}
# def analysis(num_list, number):
#     for n in num_list:
#         if n in number:
#             number[n] += 1
#         else:
#             number[n] = 1
#
#     for n in number: # далее условие if n > 1
#         print('Число', n, 'повторяется:',number[n])
#
# analysis(num_list, number)

#Сделать функцию, которая будет вызываться из генератора списков и по
#запросу к ней отдавать текущее время с задержкой в 1 сек.
#Кол-во элементов нового списка n запрашивать у пользователя.

import time
from datetime import datetime
def tek_vr():
    time.sleep(1)  # Задержка в 1 секунду
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')  # Возвращаем текущее время в формате '%Y-%m-%d %H:%M:%S'

n = int(input("Введите количество элементов нового списка: "))

# Генератор списка с вызовом функции get_current_time()
spisok= [tek_vr() for _ in range(n)]

# Выводим новый список
print(spisok)