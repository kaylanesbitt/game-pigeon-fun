import os, pickle
from trie_module import Trie
from requests import get

PICKLE_FILE = "common/dictionary.pkl"

def load_trie(): 
    url = "https://raw.githubusercontent.com/scrabblewords/scrabblewords/main/words/North-American/NWL2020.txt"
    response = get(url)

    dictionary = Trie()

    if response.status_code == 200:
        raw_data = response.text.splitlines()

        words = [row.split(" ")[0].lower() for row in raw_data if len(row.split(" ")[0]) > 2]

        for word in words: 
            dictionary.insert(word)
        
        return dictionary

    else:
        print("Failed to fetch words:", response.status_code)

def get_trie():
    """Return a persistent Trie object, loading from pickle if available."""
    if os.path.exists(PICKLE_FILE):
        with open(PICKLE_FILE, "rb") as f:
            trie = pickle.load(f)
        print("Dictionary loaded from pickle file")
    else:
        trie = load_trie()
        with open(PICKLE_FILE, "wb") as f:
            pickle.dump(trie, f)
        print("Trie built and saved to pickle file")
    return trie

dictionary = get_trie()
    