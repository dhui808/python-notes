class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

# Creating an object
my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says woof!

