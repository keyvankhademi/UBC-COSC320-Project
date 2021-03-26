

def naive_fix(text, shorties):
    tokens = text.split()
    result = [shorties[x] if x in shorties else x for x in tokens]
    return " ".join(result)
