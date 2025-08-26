
import sys
import os
import unittest

# Add the path to import main.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'myfirstpyapp')))
from main import Dog

class TestDog(unittest.TestCase):
    def test_bark(self):
        dog = Dog("Buddy", "Golden Retriever")
        self.assertEqual(dog.bark(), "Buddy says Woof!")

if __name__ == "__main__":
    unittest.main()
