import os
import sys
from myfirstpyapp.main import Dog

def main():
    print("This is my second Python application.")
    print("Calling the first application...")
    dog = Dog("Gold", "Golden Retriever")
    print(dog.bark())
    print("First application has finished execution.")
 
if __name__ == "__main__":
    main() 