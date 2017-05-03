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
    table_size = test_input[0]
    percents = np.array(test_input[1])

    table = hash.ChainedHashTable(table_size)
    table_size = table.size

    collisions = []
    collisions_summary = {}

    for percent in percents:
        for i in xrange(20):  # Insertion tests
            values_to_insert = random_generate(table_size * percent, (0, 100 * table_size))
            for value in values_to_insert:
                table.insert(value)
            collisions.append(table.collision_counter)
            table.clear()

        # for each percent group, store max, min and average collision number
        max_collision = max(collisions)
        min_collision = min(collisions)
        avg_collision = (max_collision + min_collision) / 2
        collisions_summary[percent] = (max_collision, min_collision, avg_collision)
        del collisions[:]

    pickle.dump(collisions_summary, open("test_chained.pickle", "wb"))


def start_tests():
    test_input = pickle.load(open("test_input.pickle", "rb"))
    test_chained(test_input)
