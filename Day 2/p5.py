



from abc import ABC, abstractmethod

class Shape (ABC):
    @abstractmethod #decorator

    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    # Concrete Method
    def description(self):
        return f"This shape has an area of {self.area():.2f}"


# Child Class

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
circle = Circle(9)
print(circle.area())
print(circle.perimeter())