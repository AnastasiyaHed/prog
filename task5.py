#Написать лямьда-функцию определяющую четное/нечетное.Функция принимает
#парамерт (число) и если четное, то выдает "четное", если нет-то "нечетное".

# x = int(input('Введите число: '))
# f = (lambda x: (x % 2 and 'нечетное' or 'четное'))
# print(f(x))

#Дан писок чисел. Вернуть список, где при помощи функции map() каждое число переведено
#в строку. В качестве функции map использовать lambda

#my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
#new_list = list(map(lambda x: str(x), my_list))
#print(new_list)


#При помощи функции filter() из кортежа слов отфильтровать только те, которые являются
#полиндромами (которые читаются в обе стороны).

#m = ('привет', 'дед', 'где', 'мой', 'заказ', 'иди', 'в', 'шалаш')
#nw = list(filter(lambda x: x == x[::-1], m))
#print(nw)

#Написать декоратор к 2-м любым функциям, который бы считал и выводил
#время их выполнения.

# from datetime import datetime
# def my_decor(func):
#     def wrapper():
#         print('Время выполнения ', datetime.now(func()))
#     return wrapper
#
# @my_decor
# def my_func():
#     print('Первая функция')
# @my_decor
# def my_func2():
#     print('Вторая функция')
#
# my_func()
# my_func2()
