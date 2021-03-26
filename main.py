from time import sleep

import pandas as pd

from algorithm import naive_fix

abbreviations = pd.read_csv("data/abbreviations.csv")
contractions = pd.read_csv("data/contractions.csv")
tweets = pd.read_csv("data/tweets.csv")

contractions = contractions.rename(columns={"Contraction": "Abbreviations", "Meaning": "Text"})
shorties = pd.concat([abbreviations, contractions])

tweets = tweets[:100]

shorties = {x[0]: x[1] for i, x in shorties.iterrows()}
tweets = [x[5] for i, x in tweets.iterrows()]
fixed_tweets = [naive_fix(x, shorties) for x in tweets]

for i in range(len(tweets)):

    f = True
    for a, b in shorties.items():
        if a in tweets[i].split():
            f = False
    if f:
        continue

    print("=====")
    print(tweets[i])
    print(fixed_tweets[i])
