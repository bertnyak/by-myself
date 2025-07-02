from math import pi


class Rectangle:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

class Circle:
    def __init__(self, r) -> None:
        self.r = r
    def area(self):
        return pi * self.r ** 2

class Triangle:
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
        

class Square:
    def __init__(self, a) -> None:
        self.a = a
    def area(self):
        return self.a ** 2

class Trapezoid:
    def __init__(self, a, b, h) -> None:
        self.a = a
        self.b = b  
        self.h = h
    def area(self):
        return 0.5 * (self.a + self.b) * self.h

class Parallelogram:
    def __init__(self, a, h) -> None:
        self.a = a
        self.h = h
    def area(self):
        return self.a * self.h