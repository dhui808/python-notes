class Dog:
    def __init__(self, name, breed):
        self.name = name  # Assigning 'name' to the object's 'name' attribute
        self.breed = breed # Assigning 'breed' to the object's 'breed' attribute

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an instance of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Accessing attributes and calling methods
print(f"My dog's name is {my_dog.name} and he is a {my_dog.breed}.")
my_dog.bark()

