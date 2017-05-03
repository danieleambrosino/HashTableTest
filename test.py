import pickle
import hash
import random
import numpy as np


def random_generate(values_amount, values_range):
    values = np.array([None] * values_amount)
    for i in xrange(values_amount):
        values[i] = random.randint(values_range[0], values_range[1])
    return values


def test_chained(test_input):
    hash_table_size = test_input[0]
    percents = np.array(test_input[1])

    chained_hash_table = hash.ChainedHashTable(hash_table_size)
    hash_table_size = chained_hash_table.size

    collisions = []
    collisions_dictionary = {}

    for percent in percents:
        for i in xrange(20):  # Insertion tests
            values_to_insert = random_generate(hash_table_size * percent, (0, 100 * hash_table_size))
            for value in values_to_insert:
                chained_hash_table.insert(value)
            collisions.append(chained_hash_table.collision_counter)
            chained_hash_table.clear()

        # for each percent group, store max, min and average collision number
        max_collision = max(collisions)
        min_collision = min(collisions)
        avg_collision = (max_collision - min_collision) / 2
        collisions_dictionary[percent] = (max_collision, min_collision, avg_collision)
        del collisions[:]

    pickle.dump(collisions_dictionary, open("test_chained.pickle", "wb"))


def start_tests():
    test_input = pickle.load(open("test_input.pickle", "rb"))
    test_chained(test_input)
