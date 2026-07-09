
#Syntax 
#lambda paraMeters: expression
# Lambda Functions

add_lambda = lambda a, b: a + b
print(add_lambda(60, 40))  

#Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

#Lambda with map()
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Lambda as a key in dictionary
students = {
    'name': 'Ajinkya',
    'age' : 20,
    'grade': lambda x: f"Grade : {x}%"
}
print(students['grade'](99))  