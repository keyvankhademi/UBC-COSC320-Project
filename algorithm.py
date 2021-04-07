import time


class Trie:
    def __init__(self):
        self.children = {}
        self.mark = False
        self.expanded = None

    def insert(self, string, expanded, p=0):
        # print(string, expanded, p)
        if p == len(string):
            self.mark = True
            self.expanded = expanded
            return
        if string[p] not in self.children:
            self.children[string[p]] = Trie()
        self.children[string[p]].insert(string, expanded, p+1)

    def search(self, string, p=0):
        if p == len(string) and self.mark:
            return self.expanded
        if p == len(string) or string[p] not in self.children:
            return None
        return self.children[string[p]].search(string, p+1)


def naive_fix(text, shorties):
    tokens = text.split()
    result = [shorties[x] if x in shorties else x for x in tokens]
    return " ".join(result)


def fix(text, trie):
    tokens = text.split()
    result = []
    for token in tokens:
        expanded = trie.search(token)
        result.append(expanded if expanded else token)
    return " ".join(result)


def fix_abbreviations_naive(tweets, shorties):
    return [naive_fix(x, shorties) for x in tweets]


def fix_abbreviations(tweets, shorties):
    trie = Trie()

    for string, expanded in shorties.items():
        trie.insert(string, expanded)

    return [fix(x, trie) for x in tweets]


def time_fix_abbreviations_naive(tweets, shorties):
    start = time.time()
    fix_abbreviations_naive(tweets, shorties)
    end = time.time()
    return end - start


def time_fix_abbreviations(tweets, shorties):
    start = time.time()
    fix_abbreviations(tweets, shorties)
    end = time.time()
    return end - start