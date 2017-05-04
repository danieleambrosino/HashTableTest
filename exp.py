import pickle
from test import start_tests
import matplotlib.pyplot as plt


hash_table_size = 1000
percents = (10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)

test_values = (hash_table_size, percents)

pickle.dump(test_values, open("test_input.pickle", "wb"))

start_tests()

results = open("test_result.pickle", "rb")
chained_results = pickle.load(results)
open_results = pickle.load(results)
open_collisions = open_results[0]
open_inspections = open_results[1]

# Chained hash table collisions plot
x_axis = percents
y_min = chained_results[:, 0]
y_avg = chained_results[:, 1]
y_max = chained_results[:, 2]

plt.plot(x_axis, y_min)
plt.plot(x_axis, y_avg)
plt.plot(x_axis, y_max)

plt.xlabel('Load percentage')
plt.ylabel('Collisions number')
plt.legend(['Minimum', 'Average', 'Maximum'], loc=2)
plt.show()

# Open hash table collisions plot
y_min = open_collisions[:, 0]
y_avg = open_collisions[:, 1]
y_max = open_collisions[:, 2]

plt.plot(x_axis, y_min)
plt.plot(x_axis, y_avg)
plt.plot(x_axis, y_max)

plt.xlabel('Load percentage')
plt.ylabel('Collisions number')
plt.legend(['Minimum', 'Average', 'Maximum'], loc=2)
plt.show()

# Open hash table inspection lengths
y_min = open_inspections[:, 0]
y_avg = open_inspections[:, 1]
y_max = open_inspections[:, 2]

plt.plot(x_axis, y_min)
plt.plot(x_axis, y_avg)
plt.plot(x_axis, y_max)

plt.xlabel('Load percentage')
plt.ylabel('Inspection sequence length')
plt.legend(['Minimum', 'Average', 'Maximum'], loc=2)
plt.show()
