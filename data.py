import pandas as pd


def load_data():
    abbreviations = pd.read_csv("data/abbreviations.csv")
    contractions = pd.read_csv("data/contractions.csv")
    tweets = pd.read_csv("data/tweets.csv")
    tweets = [x[5] for i, x in tweets.iterrows()]

    contractions = contractions.rename(columns={"Contraction": "Abbreviations", "Meaning": "Text"})
    shorties = pd.concat([abbreviations, contractions])
    shorties = {x[0]: x[1] for i, x in shorties.iterrows()}

    return tweets, shorties
