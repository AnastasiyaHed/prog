# 1 Декорировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'.
# Затем результат преобразовать в байтовый вид в кодировке 'Latin 1' и затем
# результат снова декорировать в строку (результат всех преобразований выводить на экран)

# byte_string = b'r\xc3\xa9sum\xc3\xa9'
# decoded_string = byte_string.decode('utf-8')
# print(decoded_string)
#
# latin_string = decoded_string.encode('latin-1')
# print(latin_string)
#
# latin_string2 = latin_string.decode('latin-1')
# print(latin_string2)


#2 Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
#Создать файл и записать в него 2 строки и закрыть файл. Затем открыть
#файл на редоктирование и дописать оставшиеся 2 строки. В итоговом файле
#должны быть 4 строки, каждая из которых должна начинаться с новой строки
#
# h = input('Введите первую строку: ')
# b = input('Введите вторую строку: ')
# s = input('Введите третью строку: ')
# d = input('Введите четвертую строку: ')
#
# with open('example.txt', 'w') as f:
#     f.write(h + '\n')
#     f.write(b + '\n')
#
# with open('example.txt', 'a') as f:
#     f.write(s + '\n')
#     f.write(d + '\n')

#3 Создать словарь в качестве ключа которого будет 6-ти значное число (id)
#а в качестве значений кортеж состоящий из 2-х элементов - имя(str), возраст(int).
#Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл.

# import json
#
# data = {
#     123456: ("Bob", 25),
#     234567: ("Robert", 30),
#     345678: ("Klark", 35),
#     456789: ("Bobby", 40),
#     567890: ("Helen", 45),
# }
#
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)


#4 Прочитать сохраненный json-файл и записать данные на диск в csv-файл,
#первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"

# import json
# import csv
# import pandas as pd
#
# with open("data.json", "r") as file:
#     data = json.load(file)
#
# with open("data.csv", "w", newline="") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["ID", "Name", "Age"])
#
#     for id, (name, age) in data.items():
#         writer.writerow([id, name, age])
#
# file = "data.csv"
# data = pd.read_csv(file) # Загрузка данных из файла в DataFrame
# phone_numbers = ['80292223322', '80291112233', '80332221133', '80449998877', '80445554422']
# data['phone'] = phone_numbers
# data.to_csv(file, index=False)


#5 Прочитать сохраненный файл csv-файл и сохранить данные в exel-файл, кроме возраста - столбец
#c этими данными не нужен.

import pandas as pd

df = pd.read_csv('data.csv', delimiter=',') # Чтение файла CSV

df = df.drop('Age', axis=1) # Удаление столбца "Age"

writer = pd.ExcelWriter('data.xlsx') # Создание объекта ExcelWriter для сохранения данных в файл Excel
df.to_excel(writer, index=False) # Сохранение данных в файл Excel
writer._save() # Закрытие объекта ExcelWriter