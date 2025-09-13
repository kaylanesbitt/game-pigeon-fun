from games import word_hunt, anagrams

def print_word_hunt_words(): 
    chars = input("Enter your board as a 16-character string, reading each row left to right, starting at the top: ")
    board = word_hunt.Board(chars.lower().replace(" ", ""))
    print(sorted(board.find_words(), key=len, reverse=True))  

def print_anagrams_words(): 
    chars = input("Enter the available characters as a string, no spaces ")
    anagram = anagrams.Anagram(chars)
    print(anagram.find_words())

def main(): 
    game = input("Enter your game: WH for word hunt, AN for anagrams ")
    match game.upper(): 
        case 'WH': 
            print_word_hunt_words()
        case 'AN': 
            print_anagrams_words()

if __name__ == "__main__": 
    main()
