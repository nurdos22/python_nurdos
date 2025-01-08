class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length ):
        super(Square, self).__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        return f"Square side length:{self.__side_length}{self.unit}, area: {self.calculate_area()}{self.unit}"

class Rectangle(Figure):
    def __init__(self, length ,width):
        super(Rectangle, self).__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        return f"Rectangle length:{self.__length}{self.unit}, width:{self.__width}{self.unit}, area {self.calculate_area()}{self.unit}"


if __name__ == "__main__":
    square1 = Square(5)
    square2 = Square(4)

    rectangle1 = Rectangle(4, 7)
    rectangle2 = Rectangle(3, 5)
    rectangle3 = Rectangle(8, 10)

    figures = [square1, square2, rectangle1, rectangle2, rectangle3]

    for figure in figures:
        print(figure.info())

