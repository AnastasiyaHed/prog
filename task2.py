string = input('Введите произвольную строку: ')

a = string[1::2]
b = string[::2]

string = string.replace(" ","")
print('Введена строка: ', string, end = '\n\n\n')

print(a, b, sep ='     ', end ='\n!!!')