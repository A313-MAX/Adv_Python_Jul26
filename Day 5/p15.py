# Components of Closure 
# 1 The Outer Function 
# 2 The Inner Function
# 3 The returned Inner Function

def multiplier(factor):
    def multiply_by_factor(x):
        return x * factor
    return multiply_by_factor

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(20))

print(double.__closure__)
print(triple.__closure__ [0].cell_contents)