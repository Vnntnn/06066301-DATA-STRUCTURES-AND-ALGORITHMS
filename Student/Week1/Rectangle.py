"""rectangle calc"""
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return (self.height * 2) + (self.width * 2)

REC = Rectangle(float(input()), float(input()))
CON = input()
print(f"{REC.calculate_area():.2f}" if CON == "area" else f"{REC.calculate_perimeter():.2f}")
