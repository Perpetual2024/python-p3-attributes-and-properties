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
    def __init__(self, name=None, breed=None):
        if name is not None:
            self.name = name  # Calls the setter
        else:
            self._name = None  # Allow initialization without name
        
        if breed is not None:
            self.breed = breed  # Calls the setter
        else:
            self._breed = None  # Allow initialization without breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or  (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        self._breed = value
