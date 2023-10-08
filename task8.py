# # Создать родительский класс auto, у которого есть атрибуты: brand, age, color,
# # mark и weight. А также методы: move, birthday и stop. Методы move и stop выводят
# # сообщения на экран move и stop, а birthday увеличивает атрибут age на 1. Атрибуты brand,
# # age и mark являются обязательными при объявлении объекта class Auto:
# class Auto:
#     def __init__(self, brand, age, color, mark, weight):
#         self.brand = brand
#         self.age = age
#         self.color = color
#         self.mark = mark
#         self.weight = weight
#
#     def move(self):
#         print("Move")
#
#     def birthday(self):
#         self.age += 1
#         print(self.age)
#
#     def stop(self):
#         print("Stop")
#
# my_car = Auto("Toyota", 3, "Red", "Mark X", 1500)
# my_car.move()
# my_car.birthday()
# my_car.stop()

#Создать 2 класса truck и car, которые являются наследниками класса auto.
#Класс truck имеет дополнительный обязательный атрибут max_load. Переопределенный
#метод move, перед появлением надписи "move" выводит надпись "attention", его
# реализацию сделать при помощи оператора super. А также дополнительный метод
#load. При его вызове происходит пауза 1 сек., затем выдается сообщение "load" и
#снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут
#max_speed и при вызове метода move, после появления надписи 'move' должна
#появиться надпись "max speed". Создать по 2 объекта для каждого из классов
#truck и car, проверить все их методы и атрибуты.

# import time
# class Auto:
#     def move(self):
#         print('move1')
#
# class Truck(Auto):
#     def __init__(self, max_load):
#         self.max_load = max_load
#
#     def move(self):
#         super().move()  # Вызов метода move() родительского класса
#         print("attention")
#         print("move")
#
#     def load(self):
#         time.sleep(1)
#         print("load")
#         time.sleep(1)
#
# class Car(Auto):
#     def __init__(self, max_speed):
#         self.max_speed = max_speed
#
#     def move(self):
#         super().move()
#         print("move")
#         print("max_speed")
#
# truck1 = Truck(5000)
# truck2 = Truck(6000)
#
# truck1.move()
# truck1.load()
# print(truck1.max_load)
#
# truck2.move()
# truck2.load()
# print(truck2.max_load)
#
# car1 = Car(200)
# car2 = Car(250)
#
# # Проверка методов и атрибутов класса Car
# car1.move()
# print(car1.max_speed)
#
# car2.move()
# print(car2.max_speed)

#Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание
#двух окружностей, вычитание радиусов произвести по модулю. Если вычитаются две окружности
#c одинаковым значением радиуса, то результатом вычмиания будет точка класса Point.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.center = Point(x, y)

    def subtract(self, other_circle):
        radius_diff = abs(self.radius - other_circle.radius)
        if radius_diff <= 0:
            # Разница радиусов должна быть положительной
            return None
        else:
            # Создаем точку с координатами разницы радиусов
            return Point(radius_diff, radius_diff)

circle1 = Circle(0, 0, 0)
circle2 = Circle(3, 0, 0)

result = circle1.subtract(circle2)

if result is None:
    print("Разница радиусов не положительна.")
else:
    print(f"Точка: ({result.x}, {result.y})")