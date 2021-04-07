from algorithm import fix_abbreviations, fix_abbreviations_naive
from data import load_data

tweets, shorties = load_data()

results = fix_abbreviations(tweets, shorties)
results_naive = fix_abbreviations_naive(tweets, shorties)

for i in range(0, len(results)):
    if results[i] != results_naive[i]:
        print("Error:\nOriginal:{}\nResult:{}\nNaive:{}\n".format(tweets[i], results[i], results_naive[i]))