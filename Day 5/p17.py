# Decorators
def simple_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")

    return wrapper

def say_hello():
    print("Hello! World!")

#Apply the decorator
decorated_hello = simple_decorator(say_hello)
decorated_hello()

@simple_decorator
def say_hi():
    print("Hi! There!, Welcome")
say_hi()