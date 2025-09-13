from trie_module import Trie
from games.scrabble_dictionary import dictionary

class Anagram: 
    letters = []

    def __init__(self, letters): 
        for letter in letters: 
            self.letters.append(letter)
    
    def find_words(self): 
        words = set()
    
        def find_words_recursive(word, indexes): 
            # find min index not in indexes
            i = 0
            while i < len(self.letters): 
                if i not in indexes: 
                    break
                else: 
                    i += 1
            
            if i == len(self.letters): 
                return
            
            word += self.letters[i]
            indexes.add(i)

            if dictionary.search(word) and len(word) > 2: 
                words.add(word)
            if dictionary.is_prefix(word): 
                find_words_recursive(word, indexes)
        
        for i in range(len(self.letters)): 
            find_words_recursive(self.letters[i], set([i]))

        return words
                


        




        
    