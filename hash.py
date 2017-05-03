from utils import *
import numpy as np


class ChainedHashTable:
    def __init__(self, length):
        if not is_prime(length):
            self.size = self.lesser_prime_number(length)
        else:
            self.size = length
        print "Hash table size:", self.size
        self.table = np.array([LinkedList()] * self.size)

    def search(self, item):
        position = item % self.size
        return self.table[position].search(item)

    def insert(self, item):
        position = item % self.size
        self.table[position].add(item)

    def delete(self, item):
        position = item % item
        if self.search(item):
            self.table[position].remove(item)

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
        i = 0
        while i < self.size:
            if self.table[index] is None or self.table[index] is -1:  # -1 is the DELETED special value
                self.table[index] = item
                return index
            i += 1
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
