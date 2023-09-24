#Сделать функцию, которая на вход принимает строку. Анализирует ее исключительно методом .isdigit(), без
#доп библиотек и переводит строку в число. Функция умеет распозновать отрицательные числа и десятичные дроби

def main():
    if text.isdigit():
        num1 = int(text)
    return 'Вы ввели положительное целое число:', num1
try:
    v = int(text)
    if v < 0:
        return 'Вы ввели отрицательное целое число:', v
except:
    list1 = list(text)
    i = ','
    if i in list1:
        new_n_name = '.'
        list1 = [a if a != i else new_n_name for a in list1]
    try:
        db = float(''.join(list1))
        if db > 0:
            return 'Вы ввели положительное дробное число:', db
        else:
            return 'Вы ввели отрицательное дробное число:', db
    except:
        return 'Вы ввели некорректное число:', text


while True:
    text = input('Введите число: ')
    if text.upper() in ("ВЫХОД", "E", "EXIT", "QUIT", "Q"):
        break
    result = main()
    print(*result)