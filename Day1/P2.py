# Parent Class 

class Animal:
    def __init__(self,name):
        self.name =name 

    def makeSound (self):
        return "Some Sound"

# Child Class   
class Cat(Animal):
    def makeSound(self):
        return f"{self.name} says meow"


# Child Class
class Cow(Animal):
    def makeSound(self):
        return f"{self.name} says moo"
    

cat = Cat ("Tom")
cow = Cow ("Jerry")

print (cat.makeSound())
print (cow.makeSound())
