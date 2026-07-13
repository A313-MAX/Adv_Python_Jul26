# Closure vs Class

def make_counter():
    count = 0

    def increment():
        # Keyword used inside nested function to indicate that a variable belongs to the nearest enclosing scope.
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter()) 
print(counter()) 


class Counter:
    def __init__(self):
        self.count = 0
        
    def increment(self):
        self.count += 1
        return self.count
counter_obj = Counter()

print(counter_obj.increment())
print(counter_obj.increment())

# Closure : Simple case, single function behavior
# Classes : 