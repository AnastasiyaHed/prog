# Создайте класс Soda (для определения типа газированной воды), принимающий 1
# аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). В
# этом классе реализуйте метод show_my_drink(), выводящий на печать Газировка и
# {ДОБАВКА} в случае наличия добавки, а иначе отобразится следующая фраза: Обычная газировка.

#
# class Soda:
#     def __init__(self, dobavka=None):
#         self.dobavka = dobavka
#
#     def show_my_drink(self):
#         if self.dobavka:
#             print("Газировка и", self.dobavka)
#         else:
#             print("Обычная газировка")
#
# soda_1 = Soda("вишня")
# soda_1.show_my_drink()
#
# soda_2 = Soda()
# soda_2.show_my_drink()

# Николаю требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого он решил создать класс TriangleChecker, принимающий
# только положительные числа. С помощью метода is_triangle() возвращаются следующие значения
# (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

class TriangleChecker:
    def __init__(self, stor1, stor2, stor3):
        if stor1 <= 0 or stor2 <= 0 or stor3 <= 0:
            self.stor1 = stor1
            self.stor2 = stor2
            self.stor3 = stor3
        else:
            print("С отрицательными числами ничего не выйдет.")

    def is_triangle(self):
        if self.stor1 + self.stor2 <= self.stor3 or self.stor2 + self.stor3 <= self.stor1 or self.stor3 + self.stor3 <= self.stor2:
            return "Жаль, но из этого треугольник не сделать."

triangle = TriangleChecker(3, 4, 5)
print(triangle.is_triangle())