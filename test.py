import pickle
import hash_tables
import random
import numpy as np


def random_generate(values_amount, values_max):
    values = np.array([None] * values_amount)
    for i in xrange(values_amount):
        values[i] = random.randint(0, values_max)
    return values


def test_chained(test_input):
    table_size = test_input[0]
    percents = test_input[1]

    table = hash_tables.ChainedHashTable(table_size)
    table_size = table.size

    collisions = []
    summary = np.array([[0, 0, 0]])

    for percent in percents:
        for i in xrange(20):
            values_to_insert = random_generate(table_size * percent / 100, table_size * 100)
            for value in values_to_insert:
                table.insert(value)
            collisions.append(table.collision_counter)
            table.clear()

        max_collision = max(collisions)
        min_collision = min(collisions)
        avg_collision = (max_collision + min_collision) / 2

        summary = np.append(summary, [[min_collision, avg_collision, max_collision]], axis=0)
        collisions = []

    summary = np.delete(summary, 0, 0)
    print summary
    return summary


def test_open(test_input):
    table_size = test_input[0]
    percents = np.array(test_input[1])

    table = hash_tables.OpenHashTable(table_size)
    table_size = table.size

    collisions = []
    inspection_sequence_lengths = []

    summary = {}

    for percent in percents:
        for i in xrange(20):
            # generating random values to be inserted
            values_to_insert = random_generate(table_size * percent, 100 * table_size)

            # inserting random values in hash table
            for value in values_to_insert:
                table.insert(value)

            collisions.append(table.collision_counter)
            inspections_sequence_lengths.append(table.max_inspection_length)
            table.clear()

        max_collision = max(collisions)
        min_collision = min(collisions)
        avg_collision = (max_collision + min_collision) / 2

        summary[percent] = (max_collision, min_collision, avg_collision)
        del collisions[:]

    return summary


def start_tests():
    test_input = pickle.load(open("test_input.pickle", "rb"))

    chained_results = test_chained(test_input)
    # open_results = test_open(test_input)

    result_file = open("test_result.pickle", "wb")
    pickle.dump(chained_results, result_file)
    # pickle.dump(open_results, result_file)
    result_file.close()
