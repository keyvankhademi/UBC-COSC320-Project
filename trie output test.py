from algorithm import fix_abbreviations, fix_abbreviations_naive
from data import load_data

tweets, shorties = load_data()

results = fix_abbreviations(tweets, shorties)

for i in range(0, 20):
    print("Original:{}\nResult:{}".format(tweets[i], results[i]))