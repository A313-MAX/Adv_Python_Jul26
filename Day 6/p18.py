# Loops : Allows us to iterate over collection of items

fruits = ["apple", "banana", "cherry"] 
for fruit in fruits:
    print(fruit)


# for loop with range
for i in range(5):
    print(i)


# for loop with dictionary
person = {'name': 'Ajinkya', 'age': 19,'city':'Mumbai'}
for key,value in person.items():
    print(f"{key}:{value}")