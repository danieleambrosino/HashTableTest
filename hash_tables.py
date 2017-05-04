from linked_list import *
import numpy as np


def is_prime(number):
    divisor = number - 1
    while divisor > 0:
        if number % divisor == 0:
            return False
        divisor -= 1
    return True


class ChainedHashTable:
    def __init__(self, length):
        if not is_prime(length):
            self.size = self.lesser_prime_number(length)
        else:
            self.size = length
        print "Hash table size:", self.size
        self.table = np.array([])
        for i in xrange(self.size):
            self.table = np.hstack((self.table, LinkedList()))
        self.collision_counter = 0

    def search(self, item):
        position = item % self.size
        return self.table[position].search(item)

    def insert(self, item):
        position = item % self.size
        current_list = self.table[position]
        if not current_list.is_empty():
            self.collision_counter += 1

        current_list.add(item)

    def delete(self, item):
        position = item % item
        if self.search(item):
            self.table[position].remove(item)

    def clear(self):
        self.table = np.array([])
        for i in xrange(self.size):
            self.table = np.hstack((self.table, LinkedList()))
        self.collision_counter = 0

    @staticmethod
    def lesser_prime_number(number):
        result = number - 1
        while result > 0:
            denominator = result - 1
            while result % denominator != 0:
                denominator -= 1
            if denominator == 1:
                return result
            result -= 1
        return result


class OpenHashTable:
    def __init__(self, length):
        if not is_prime(length):
            self.size = self.greater_prime_number(length)
        else:
            self.size = length
        print "Hash table size:", self.size

        self.table = np.array([None] * self.size)
        self.collision_counter = 0
        self.max_inspection_length = 0
        self.min_inspection_length = 0

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
        inspection_counter = 0

        while inspection_counter < self.size:
            if self.table[index] is None or self.table[index] is -1:  # -1 is the DELETED special value
                self.table[index] = item
                return index
            inspection_counter += 1

            # update class attributes
            self.collision_counter += 1
            if inspection_counter > self.max_inspection_length:
                self.max_inspection_length = inspection_counter
            elif inspection_counter < self.min_inspection_length:
                self.min_inspection_length = inspection_counter

            index = (index + 1) % self.size

        print "Hash table overflow"
        return None

    def delete(self, item):
        search_result = self.search(item)
        if search_result is not None:
            self.table[search_result] = -1  # using -1 as DELETED special value
            return search_result
        print "No elements deleted"
        return None

    def clear(self):
        self.table = [None] * self.size
        self.collision_counter = 0
        self.max_inspection_length = 0
        self.min_inspection_length = 0

    @staticmethod
    def greater_prime_number(number):
        result = number + 1
        while True:
            denominator = result - 1
            while result % denominator != 0:
                denominator -= 1
            if denominator == 1:
                return result
            result += 1