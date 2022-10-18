class Figure:

    unit = 'cm'

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length
        self.perimeter = self.calculate_perimeter()

    def calculate_perimeter(self):
        return self.__side_length * 4

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def info(self):
        print(f'Square side length: {self.__side_length}{self.unit}, Perimeter: {self.perimeter}{self.unit}, '
              f'Area: {self.calculate_area()}{self.unit}')


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
        self.perimeter = self.calculate_perimeter()

    def calculate_perimeter(self):
        return (self.__length + self.__width) * 2

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f'Rectangle length: {self.__length}{self.unit}, Width: {self.__width}{self.unit}, '
              f'Perimeter: {self.perimeter}{self.unit}, 'f'Area: {self.calculate_area()}{self.unit}')


square1 = Square(7)
square2 = Square(4)
rectangle1 = Rectangle(4, 7)
rectangle2 = Rectangle(7, 9)
rectangle3 = Rectangle(2, 4)

figures = [square1, square2, rectangle1, rectangle2, rectangle3]

for i in figures:
    i.info()
