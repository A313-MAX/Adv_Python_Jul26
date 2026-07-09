# First - Create Functions

# Assigning a function to a variable

def say_hello(name):
    return f"Hello, {name}!"

# Assigning the function to a variable (without parentheses)

greet = say_hello

print (greet("Ajinkya"))  
print (say_hello("Ajinkya"))

#2 Passing a function as an argument 

def apply_operation(func, value):
    return func(value)

def double(x):
    return x * 2

print(apply_operation(double, 5))  

# Returning a function from another function

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(20)
print(double(5))  

#4 Storing functions in a data structure

operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
}
print(operations['add'](5, 3))
print(operations['subtract'](5, 3))