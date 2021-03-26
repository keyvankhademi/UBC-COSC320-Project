import pandas as pd
from algorithm import time_fix_abbreviations
import matplotlib.pyplot as plt

abbreviations = pd.read_csv("data/abbreviations.csv")
contractions = pd.read_csv("data/contractions.csv")
tweets = pd.read_csv("data/tweets.csv")

contractions = contractions.rename(columns={"Contraction": "Abbreviations", "Meaning": "Text"})
shorties = pd.concat([abbreviations, contractions])
shorties = {x[0]: x[1] for i, x in shorties.iterrows()}

tweets = tweets[:100000]
tweets = [x[5] for i, x in tweets.iterrows()]

# fixed_tweets = [naive_fix(x, shorties) for x in tweets]

time_data_x = []
time_data_y = []

for i in range(0, 100000, 1000):
    print(i)
    # df = tweets[:i]
    # tweets_list = [x[5] for j, x in df.iterrows()]
    time_data_x.append(i)
    time_data_y.append(time_fix_abbreviations(tweets[:i], shorties))


plt.plot(time_data_x, time_data_y)
plt.xlabel("n (number of tweets)")
plt.ylabel("t (execution time in seconds)")
plt.title("Execution Time of Naive Algorithm")
plt.show()
