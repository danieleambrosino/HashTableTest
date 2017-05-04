from linked_list import *


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
            print "You inserted", length, "but actual chained table size is", self.size
        else:
            self.size = length

        self.table = []
        for i in xrange(self.size):
            self.table.append(LinkedList())

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
        self.table = []
        for i in xrange(self.size):
            self.table.append(LinkedList())
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
            print "You inserted", length, "but actual open hash table size is", self.size
        else:
            self.size = length

        self.table = [None] * self.size
        self.collision_counter = 0
        self.inspection_counter = 0

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
        if self.table[index] is None or self.table[index] is -1:
            self.table[index] = item
            return index

        self.collision_counter += 1
        inspection = 0
        while inspection < self.size:
            if self.table[index] is None or self.table[index] is -1:
                self.table[index] = item
                return index
            else:
                self.inspection_counter += 1
                index = (index + 1) % self.size
                inspection += 1

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
        self.collision_counter = 0
        self.inspection_counter = 0

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
