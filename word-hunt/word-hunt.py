from dictionary import dictionary

class Board: 
    letters: list[list[str]]

    def __init__(self, input): 
        self.letters = []
        #default 4x4
        row = []
        for i in input: 
            row.append(i)
            if len(row) == 4: 
                self.letters.append(row)
                row = []

    def toString(self): 
        for row in self.letters: 
            print(row)
    
    def getLetter(self, x, y): 
        return self.letters[x][y]

    def inBoard(self, x, y): 
        if x > -1 and y > -1 and x < 4 and y < 4: 
            return True
    

    
    def find_words(self): 

        words = set()
        moves = [
        (-1,  0),  # Up
        ( 1,  0),  # Down
        ( 0, -1),  # Left
        ( 0,  1),  # Right
        (-1, -1),  # Up-Left (diagonal)
        (-1,  1),  # Up-Right (diagonal)
        ( 1, -1),  # Down-Left (diagonal)
        ( 1,  1)   # Down-Right (diagonal)
        ]

        def dfs_recursive(x, y, path, visited): 
            path += self.getLetter(x, y)
            visited.add((x,y))
            if dictionary.search(path): 
                words.add(path)
            if dictionary.is_prefix(path): 
                #check possible moves 
                for dx, dy in moves: 
                    if self.inBoard(x + dx, y + dy) and (x+dx, y+dy) not in visited: 
                        dfs_recursive(x+dx, y+dy, path, visited.copy())
            

        for x in range(4): 
            for y in range(4): 
                dfs_recursive(x, y, "", set())
        

        return sorted(list(words), key=len, reverse=True)
        

def main(): 
    chars = input("Enter your board: ")

    board = Board(chars)

    board.toString()

    print(board.find_words())
    

if __name__ == "__main__": 
    main()

    






