#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        # if (type(name)) in str and 1<= len(name) <= 25:
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}.")
            self._name = name
        else:
            print("Name must be a string between 1 and 25 characters.")

dog = Dog("Fido")
print(dog.get_name())


# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
#  isinstance(object, type)
