# Function body need to be idendented.
# * The standard is 4 spaces per indentation level.
# *	You can use tabs, but spaces are preferred (and more consistent across editors).

def greet(name):
    print(f"Hello, {name}!")
    return f"your name is {name}"

result = greet("Jack")
print(f"result={result}")
