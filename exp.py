import pickle
from test import start_tests
import matplotlib.pyplot as plt


hash_table_size = 1000
percents = (10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)

test_values = (hash_table_size, percents)

pickle.dump(test_values, open("test_input.pickle", "wb"))

start_tests()

results = pickle.load(open("test_result.pickle", "rb"))

x_axis = percents
y_min = results[:, 0]
y_avg = results[:, 1]
y_max = results[:, 2]

plt.plot(x_axis, y_min)
plt.plot(x_axis, y_avg)
plt.plot(x_axis, y_max)

plt.xlabel('Load percentage')
plt.ylabel('Collisions number')
plt.legend(['Minimum', 'Average', 'Maximum'])
plt.show()
