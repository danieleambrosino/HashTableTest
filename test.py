import pickle
import hash
import random


def random_generate(values_amount, values_range):
    values = [None] * values_amount
    for i in xrange(values_amount):
        values[i] = random.randint(values_range[0], values_range[1])
    return values


def test_chained(test_input):
    hash_table_size = test_input[0]
    percents = test_input[1]

    chained_hash_table = hash.ChainedHashTable(hash_table_size)
    hash_table_size = chained_hash_table.size

    for percent in percents:
        for i in xrange(20):
            values_to_insert = random_generate(hash_table_size * percent, (0, 100 * hash_table_size))
            for value in values_to_insert:
                chained_hash_table.insert(value)


def start_tests():
    test_input = pickle.load(open("test_input.pickle", "rb"))
    test_chained(test_input)
