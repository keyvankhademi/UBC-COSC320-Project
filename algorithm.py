import time


def naive_fix(text, shorties):
    tokens = text.split()
    result = [shorties[x] if x in shorties else x for x in tokens]
    return " ".join(result)


def fix_abbreviations(tweets, shorties):
    return [naive_fix(x, shorties) for x in tweets]


def time_fix_abbreviations(tweets, shorties):
    start = time.time()
    fix_abbreviations(tweets, shorties)
    end = time.time()
    return end - start
