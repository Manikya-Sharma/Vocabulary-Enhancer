import pickle

def add_word(word):
    word = word.capitalize()
    f = open('excluded_words.dat','rb+')
    existing = pickle.load(f)
    if word in existing:
        f.close()
        return True
    existing.append(word)
    f.truncate()
    f.seek(0)
    pickle.dump(existing,f)
    f.close()
    return True

def is_excluded(word):
    f = open('excluded_words.dat','rb+')
    data = pickle.load(f)
    if word in data:
        return True
    else:
        return False