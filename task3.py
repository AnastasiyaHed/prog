#Ввести предложение состоящее из двух слов. Поменять местами слова, добавить
#восклицательный знак в начало и конец, слова разделить 3 символами (пробел,
# восклицательный знак и еще пробел), вывести итоговое предложение на экран.
# Задание необходимо выполнить 3-мя разными способами форматирования.

i = 0
spisok =[]

while i < 2:
    string = input('Enter the word: ')
    spisok.append(string)
    i += 1

result = "!%s ! %s!" % (spisok[1], spisok[0])
print(result)

result1 = '!{1} ! {0}!'.format(spisok[0], spisok[1])
print(result1)

result2 =f'!{spisok[1]} ! {spisok[0]}!'
print(result2)

#########################################################

# Написать программу, которая получит имя и возраст пользователя, проверяет
# возраст и выдает приветственное сообщение в зависимости от возраста:
#     - меньше нуля или ноль или не число: "Ошибка, повторите ввод";
#     - больше 0 до 10 не включая: "Привет, шкет Имя";
#     - от 10 до 18 включая: "Как жизнь, имя?":
#     - больше 18 и меньше 100: "Что желаете, Имя?"
#     - в противном случае: "Имя, вы лжете - в наше время столько не живут..."
while True:
    name = input('Введите Ваше имя: ')
    age = input('Введите Ваш возраст: ')
    age = int(age)

    if age <= 0 or age == int:
        print('Ошибка, повторите ввод')
    elif 0 < age < 10:
        print('Привет, шкет', name)
    elif 10 <= age < 19:
        print('Как жизнь,', name,'?')
    elif 19 <= age < 100:
        print('Что желаете,', name,'?')
    else:
        print(name,', Вы лжете - в наше время столько не живут..."')

##############################################################################

# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до
# n включая n). Реализовать в 2-х вариантах: используя цикл while и цикл for

# n = int(input('Введите число'))
# s = []
# i = 0
# while i < n:
#     i += 1
#     a = i**3
#     s.append(a)
#     print(a)
# print('n =',n)
# print('Сумма квадратов чисел от 1 до', n, 'включая', n, '=', sum(s))

n = int(input('Введите число'))
s = []

for i in range(1, n+1):
    a = i**3
    s.append(a)
print(s)
print('n =',n)
print('Сумма квадратов чисел от 1 до', n, 'включая', n, '=', sum(s))

##########################################################################

import random

i = 0

num = random.randint(1, 10)
print('Угадайте число от 1 до 10 за 3 попытки ')

while i < 3:
    n = int(input('Введи число: '))
    i += 1

    if n < num:
        print('Ваше число меньше.')
    if n > num:
        print('Ваше число больше.')
    if n == num:
        break

if n == num:
    print('Вы угадали число, использовав {0} попыток!'.i)
else:
    print('Вы не угадали. Число = {0}'.format(num))
