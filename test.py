import pickle
import hash_tables
import random
import numpy as np


def test_chained(test_input):
    table_size = test_input[0]
    percents = test_input[1]

    table = hash_tables.ChainedHashTable(table_size)
    table_size = table.size

    collisions = []
    summary = np.array([[0, 0, 0]])

    for percent in percents:
        for i in xrange(20):
            # generating random values to be inserted
            values_to_insert = random.sample(range(table_size * 100), table_size * percent / 100)

            for value in values_to_insert:
                table.insert(value)
            collisions.append(table.collision_counter)
            table.clear()

        max_collision = max(collisions)
        min_collision = min(collisions)
        avg_collision = sum(collisions) / len(collisions)

        summary = np.append(summary, [[min_collision, avg_collision, max_collision]], axis=0)
        collisions = []

    summary = np.delete(summary, 0, 0)
    return summary


def test_open(test_input):
    table_size = test_input[0]
    percents = test_input[1]

    table = hash_tables.OpenHashTable(table_size)
    table_size = table.size

    collisions = []
    inspection_sequence_lengths = []

    collisions_summary = np.array([[0, 0, 0]])
    inspections_summary = np.array([[0, 0, 0]])

    for percent in percents:
        for i in xrange(20):
            # generating random values to be inserted
            values_to_insert = random.sample(range(table_size * 100), table_size * percent / 100)

            # inserting random values in hash table
            for value in values_to_insert:
                table.insert(value)

            collisions.append(table.collisions_counter)
            inspection_sequence_lengths.append(table.inspections[:])
            table.clear()

        max_collision = max(collisions)
        min_collision = min(collisions)
        avg_collision = sum(collisions) / len(collisions)

        max_inspection = max(max(v) for v in inspection_sequence_lengths)
        min_inspection = min(min(v) for v in inspection_sequence_lengths)
        avg_inspection = sum(sum(v) / len(v) for v in inspection_sequence_lengths) / len(inspection_sequence_lengths)

        collisions_summary = np.append(collisions_summary, [[min_collision, avg_collision, max_collision]], axis=0)
        inspections_summary = np.append(inspections_summary, [[min_inspection, avg_inspection, max_inspection]], axis=0)

        collisions = []
        inspection_sequence_lengths = []

    collisions_summary = np.delete(collisions_summary, 0, 0)
    inspections_summary = np.delete(inspections_summary, 0, 0)
    return collisions_summary, inspections_summary


def start_tests():
    test_input = pickle.load(open("test_input.pickle", "rb"))

    chained_results = test_chained(test_input)
    open_results = test_open(test_input)

    result_file = open("test_result.pickle", "wb")
    pickle.dump(chained_results, result_file)
    pickle.dump(open_results, result_file)
    result_file.close()
