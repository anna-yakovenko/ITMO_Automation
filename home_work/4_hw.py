# 1.	создайте класс прямоугольника.
# a.	атрибуты - прямоугольнику можно задать ширину и высоту
# b.	методы - реализуйте 2 метода:
# i.	расчет площади прямоугольника
# ii.	расчет периметра прямоугольника
# c.	создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width*self.height)

    def perimeter(self):
        print(2*(self.width+self.height))


rectangle1 = Rectangle(width=5, height=10)
rectangle2 = Rectangle(width=3, height=2)
rectangle3 = Rectangle(width=7, height=10)
rectangle1.area()
rectangle1.perimeter()
rectangle2.perimeter()
rectangle2.area()
rectangle3.area()
rectangle3.perimeter()


# 2.	Создайте класс Math.
# a.	Создайте два атрибута — a и b.
# b.	Напишите методы
# i.	addition — сложение,
# ii.	multiplication — умножение,
# iii.	division — деление,
# iv.	subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, a, b):
        return self.a + self.b
        print (addition(4,5))


    def multiplication(self):
        print(self.a*self.b)

    def division(self):
        print(self.a/self.b)

    def subtraction(self):
        print(self.a-self.b)










