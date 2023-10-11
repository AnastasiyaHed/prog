import sys

try:
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
except ValueError:
    print("Вы ввели не число")
    sys.exit()  # Программа закончится, если сработает except ValueError

c = (input('Введите операцию вычисления -, +, *, /, : '))
try:
    def arithmetic(a, b, c):
        d = None
        if c == '/' and b == 0:
            print('На 0 делить нельзя!')
        elif c == '-':
            d = a - b
        elif c == '+':
            d = a + b
        elif c == '/':
            d = a / b
        elif c != '/' and c != '-' and c != '+' and c != '*':
            print('неизвестная операция')
        else:
            c = a * b
        return d


    z = arithmetic(a, b, c)
    print(z)
except:
    print('Произошла ошибка')