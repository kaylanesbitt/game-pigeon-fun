import os
import pickle
import requests
from trie_module import Trie

PICKLE_FILE = "dictionary.pkl"

def get_trie(): 
    url = "https://raw.githubusercontent.com/scrabblewords/scrabblewords/main/words/North-American/NWL2020.txt"
    response = requests.get(url)

    dictionary = Trie()

    if response.status_code == 200:
        raw_data = response.text.splitlines()

        words = [row.split(" ")[0].lower() for row in raw_data if len(row.split(" ")[0]) > 2]

        for word in words: 
            dictionary.insert(word)
        
        return dictionary

    else:
        print("Failed to fetch words:", response.status_code)
    
        
    
dictionary = get_trie()
    