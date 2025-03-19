# Defining a function
def greet(name):
    print("Hello, " + name + "!")

# Calling the function
greet("Alice") # Outputs: hello alice
greet("Bob") # Outputs hello bob

# Functions can also return values!
def add_numbers(x, y):
    return x + y

result = add_numbers(10, 5)
print(result)  # Outputs x+y

# Functions take input(Parameters) and give out output.