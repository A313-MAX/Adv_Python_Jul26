# Higher- order functions: Functions that either take other functions as arguments or return a function as a result.

def apply_twice(func, value):
    return func(func(value))

def add_two(x):
    return x + 2

print(apply_twice(add_two , 10))


# 2. Return a  finction 

def make_logger(prefix):
    def logger(message):
        print(f"{prefix}: {message}")
    return logger

info_logger = make_logger("INFO")
info_logger("System Started")