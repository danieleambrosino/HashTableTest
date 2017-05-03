import pickle
from test import start_tests


hash_table_size = 1000
percents = (10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)

test_values = (hash_table_size, percents)

pickle.dump(test_values, open("test_input.pickle", "wb"))

start_tests()
