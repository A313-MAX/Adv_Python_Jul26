def simple_generator():
    print ("Step 1 : 1st yield")
    yield 1

    print ("Step 2 : 2nd yield")
    yield 2

    print ("Step 3 : 3rd yield")
    yield 3

    print ("Generator is Done ")

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))