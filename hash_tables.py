from linked_list import *
from math import sqrt


def is_prime(number):
    if number == 2:
        return True
    if number <= 1 or number % 2 == 0:
        return False
    square_root = int(sqrt(number)) + 1
    for divisor in xrange(3, square_root, 2):
        if number % divisor == 0:
            return False
    return True


class ChainedHashTable:
    def __init__(self, length):
        if not is_prime(length):
            self.size = self.lesser_prime_number(length)
            print "You inserted", length, "but actual chained table size is", self.size
        else:
            self.size = length

        self.table = [None] * self.size
        for i in xrange(self.size):
            self.table[i] = LinkedList()

        self.collision_counter = 0

    def search(self, item):
        position = item % self.size
        return self.table[position].search(item)

    def insert(self, item):
        position = item % self.size
        current_list = self.table[position]
        if not current_list.is_empty():
            self.collision_counter += 1

        current_list.insert(item)

    def remove(self, item):
        position = item % self.size
        self.table[position].remove(item)

    def clear(self):
        self.table = [None] * self.size
        for i in xrange(self.size):
            self.table[i] = LinkedList()
        self.collision_counter = 0

    @staticmethod
    def lesser_prime_number(number):
        while not is_prime(number):
            number -= 1
        return number


class OpenHashTable:
    # -1 is the "DELETED" special value

    def __init__(self, length):
        if not is_prime(length):
            self.size = self.greater_prime_number(length)
            print "You inserted", length, "but actual open hash table size is", self.size
        else:
            self.size = length

        self.table = [None] * self.size
        self.collisions_counter = 0
        self.inspections = []

    def search(self, item):
        index = item % self.size
        i = 0
        while self.table[index] is not None and i < self.size:
            if self.table[index] == item:
                return index
            i += 1
            index = (index + 1) % self.size
        return None

    def insert(self, item):
        index = item % self.size
        inspections = 0
        while inspections < self.size:
            if self.table[index] is None or self.table[index] is -1:
                self.table[index] = item
                self.inspections.append(inspections)
                return index
            else:
                self.collisions_counter += 1
                index = (index + 1) % self.size
                inspections += 1

        print "Hash table overflow!"
        return None

    def remove(self, item):
        search_result = self.search(item)
        if search_result is not None:
            self.table[search_result] = -1
            return search_result
        return None

    def clear(self):
        self.table = [None] * self.size
        self.collisions_counter = 0
        self.inspections = []

    @staticmethod
    def greater_prime_number(number):
        while not is_prime(number):
            number += 1
        return number
