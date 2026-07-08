# Descriptor is like a security guard for attributes. It allows you to control the access and modification of an attribute in a class.

class PositiveNumber:
    """
        A descriptor which ensures that the value assigned to it is a positive number.
    """
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self,obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name,None)
    
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be a positive number.")
        
        obj.__dict__[self.name] = value

    def __delete__(self, obj):
        del obj.__dict__[self.name]

class Product:
    price = PositiveNumber()
    stock = PositiveNumber()

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

product = Product("Laptop", 78500, 10)
print(f"Product: {product.name}, Price: {product.price}, Stock: {product.stock}")

try:
    product.price = -80000
except ValueError as e:
    print(f"Error: {e}")