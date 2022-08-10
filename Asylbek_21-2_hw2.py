class Figure:

    unit = 'cm'
    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError('Wrong value type it must be positive (float or integer)')
        else:
            self.__perimeter = value
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
    def info(self):
        pass

class Square(Figure):

    def __init__(self, side_length):
        super().__init__()
        self.__side_length = int(side_length)
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__side_length ** 2

    def calculate_perimeter(self):
        return self.__side_length * 4

    def info(self):
        print(f'Square side length: {str(self.__side_length) + self.unit}, perimeter:'
              f'{str(self.perimeter) + self.unit}, area: {str(self.calculate_area()) + self.unit}.')

class Rectangle(Figure):

    def __init__(self, length, width):
        super().__init__()
        self.__length = int(length)
        self.__width = int(width)
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return self.__length * 2 + self.__width * 2

    def info(self):
        print(f'Rectangle length: {str(self.__length) + self.unit}, width: {str(self.__width) + self.unit}, '
              f'perimeter: {str(self.perimeter) + self.unit}, area: {str(self.calculate_area()) + self.unit}')

figures = [
    Square(5),
    Square(6),
    Rectangle(2, 4),
    Rectangle(5, 8),
    Rectangle(7, 10)
]

for figure in figures:
    figure.info()
