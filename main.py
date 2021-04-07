import matplotlib.pyplot as plt

from algorithm import time_fix_abbreviations_naive, time_fix_abbreviations
from data import load_data

tweets, shorties = load_data()

time_data_x = []
time_data_y = []
time_data_y_naive = []

for i in range(0, 100000, 1000):
    print(i)
    time_data_x.append(i)
    time_data_y.append(time_fix_abbreviations(tweets[:i], shorties))
    time_data_y_naive.append(time_fix_abbreviations_naive(tweets[:i], shorties))

plt.plot(time_data_x, time_data_y)
plt.plot(time_data_x, time_data_y_naive)
plt.xlabel("n (number of tweets)")
plt.ylabel("t (execution time in seconds)")
plt.title("Execution Time of Naive Algorithm")
plt.show()
