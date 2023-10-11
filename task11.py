# # Создать генератор геометрической прогресии
#
# import pdb
#
# a = int(input('Введите начальное значение: '))
# b = int(input('Введите знаменатель: '))
# n = int(input('До какого элемента считать геометрическую прогрессию? '))
#
# def generator(start, znamenatel):
#     a = start # переменная а будет перезаписываться
#     while True:
#         yield a
#         a *= znamenatel
# pdb.set_trace()
# # Создаем генератор геометрической прогрессии
# progression = generator(a, b)
#
# # Генерируем первые n элементов прогрессии и выводим их
# for _ in range(n):
#     print(next(progression))

# Написать регулярку правила валидации имейлов "username@hostname"
#
# - username может содержать в себе:
# латиницу
# цифры
# знаки a-zA-Z0-9.!# %&'*+-/=?^_`{|}~
# точку, за исключением первого и последнего знака, которая не пожет повторяться
#
# hostname состоит из нескольких компонентов, разделенных точной и не превышающих 63 символа.
# Компоненты в свою очередь, состоят из латинских букв, цифр, дефисов, причем дейфисы не могут
# быть вначале или в конце компонента


import re

email = input('Введите email: ')

def check_email(email):
    pattern = r'^[=?^_{|}~`/a-zA-Z0-9!# %&*+-][a-zA-Z0-9.!# %&*+-/=?^_{|}~`]*[=?^_{|}~`/a-zA-Z0-9!# %&*+-]@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]{1,63})+$'
    if re.match(pattern, email): # используется для проверки соответствия строки string заданному регулярному выражению pattern. Она ищет соответствие между началом строки и регулярным выражением.
        print("Email валидный")
    else:
        print("Email невалидный")

check_email(email)