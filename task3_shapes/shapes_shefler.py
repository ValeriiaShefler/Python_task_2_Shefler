#Задача 3: Иерархия классов геометрических фигур
from abc import ABC, abstractmethod
from math import pi
from typing import Union

class Shape(ABC):
    #базовый класс для всех фигур
    
    @abstractmethod
    #вычисление площади
    def area(self) -> float:
        pass
    
    @abstractmethod
    #вычисление периметра
    def perimeter(self) -> float:
        pass
    
    def compare_area(self, other: 'Shape') -> str:
        #сравнение площадей фигуры self (текушей) с other (другой)
        # возвращает строку с пояснением
        if self.area() > other.area():
            return f"Площадь {self.__class__.__name__} ({self.area():.2f}) > площади {other.__class__.__name__} ({other.area():.2f})"
        elif self.area() < other.area():
            return f"Площадь {self.__class__.__name__} ({self.area():.2f}) < площади {other.__class__.__name__} ({other.area():.2f})"
        else:
            return f"Площади равны: {self.area():.2f}"
    
    def compare_perimeter(self, other: 'Shape') -> str:
        #сравнение перметра фигуры self (текушей) с other (другой)
        # возвращает строку с пояснением
        if self.perimeter() > other.perimeter():
            return f"Периметр {self.__class__.__name__} ({self.perimeter():.2f}) > периметра {other.__class__.__name__} ({other.perimeter():.2f})"
        elif self.perimeter() < other.perimeter():
            return f"Периметр {self.__class__.__name__} ({self.perimeter():.2f}) < периметра {other.__class__.__name__} ({other.perimeter():.2f})"
        else:
            return f"Периметры равны: {self.perimeter():.2f}"


class Square(Shape):
       
    def __init__(self, side: float):
        #инициализация квадрата по длине стороны
        #обработка при ошбке
        if side <= 0:
            raise ValueError("Сторона должна быть положительным числом")
        self.side = side
    
    def area(self) -> float:
        # вычисление площади квадрата
        return self.side ** 2
    
    def perimeter(self) -> float:
        # вычисление периметра квадрата
        return 4 * self.side
    
    # пояснение касательно конкретного квадрата
    def __str__(self) -> str:
        return f"Квадрат (сторона={self.side})"


class Rectangle(Shape):
    
    def __init__(self, width: float, height: float):
        #инициализация прямоугольника по длине сторон
        #обработка при ошбке
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        # площадь
        return self.width * self.height
    
    def perimeter(self) -> float:
        #периметр
        return 2 * (self.width + self.height)
    
    def __str__(self) -> str:
        return f"Прямоугольник (ширина={self.width}, высота={self.height})"


class Triangle(Shape):
    
    def __init__(self, side_a: float, side_b: float, side_c: float):
        # инициализация трегуольник апо трем сторонам
        #обработк апри ошибке (в том числе на неравенство, чтобы треугольник существовал)
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Все стороны должны быть положительными числами")
        if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
            raise ValueError("Стороны не образуют треугольник")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self) -> float:
        #площадь треугольника (формула Герона)
        p = self.perimeter() / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
    
    def perimeter(self) -> float:
        # периметр
        return self.side_a + self.side_b + self.side_c
    
    def __str__(self) -> str:
        return f"Треугольник (стороны={self.side_a}, {self.side_b}, {self.side_c})"


class Circle(Shape):
    
    def __init__(self, radius: float):
        #инициализация круга по радиусу и обработка ошибок
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius
    
    def area(self) -> float:
        #площадь круга
        return pi * self.radius ** 2
    
    def perimeter(self) -> float:
        #периметр круга
        return 2 * pi * self.radius
    
    def __str__(self) -> str:
        return f"Круг (радиус={self.radius})"


def main():
    # Тестирование
    
    # Создаем фигуры
    square = Square(6)
    rectangle = Rectangle(3, 7)
    triangle = Triangle(2, 4, 4)
    circle = Circle(7)
    
    shapes = [square, rectangle, triangle, circle]
    
    print("=" * 60)
    print("Информация о фигурах:")
    print("=" * 60)
    
    for shape in shapes:
        print(f"\n{shape}")
        print(f"  Площадь: {shape.area():.2f}")
        print(f"  Периметр: {shape.perimeter():.2f}")
    
    # Сравнение площадей
    print("\n" + "=" * 60)
    print("Сравнение площадей:")
    print("=" * 60)
    print(square.compare_area(rectangle))
    print(square.compare_area(circle))
    print(triangle.compare_area(square))
    print(circle.compare_area(rectangle))
    
    # Сравнение периметров
    print("\n" + "=" * 60)
    print("Сравнение периметров:")
    print("=" * 60)
    print(square.compare_perimeter(rectangle))
    print(rectangle.compare_perimeter(circle))
    print(triangle.compare_perimeter(square))
    print(circle.compare_perimeter(triangle))
    
    # сравнение одинаковых по площади и периметру квадрата и прямоугольника
    print("\n" + "=" * 60)
    print("Сравнение одинаковых по площади и периметру квадрата и прямоугольника (3 на 3):")
    print("=" * 60)
    square2 = Square(3)
    rectangle2 = Rectangle(3, 3)
    print(square2.compare_area(rectangle2))
    print(square2.compare_perimeter(rectangle2))


if __name__ == "__main__":
    main()