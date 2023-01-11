import pytest
from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dog_queue.enqueue(animal)
        elif isinstance(animal, Cat):
            self.cat_queue.enqueue(animal)

    def dequeue(self, pref):
        if pref == "dog":
            return self.dog_queue.dequeue()
        elif pref == "cat":
            return self.cat_queue.dequeue()
        return None


class Cat:
    def __str__(self):
        return 'cat'


class Dog:
    def __str__(self):
        return 'dog'
