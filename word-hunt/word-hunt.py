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
    

    
    def traverse(self): 

        vis = [[False for i in range(4)] for j in range(4)]
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]

        def isValid(self, x, y): 
            if self.inBoard(x,y) == False: 
                return False
            elif vis[x][y]: 
                return False
            return True

        def dfs(self, x=0, y=0): 
            st = []
            st.append([x,y])

            while len(st) > 0: 
                curr = st.pop()
                row,col = curr[0], curr[1]
                if (isValid(self,row,col) == False): 
                    continue
            
                vis[row][col] = True

                print(self.getLetter(row, col), end="")

                # push all valid moves
                for i in range(4):
                    adjx = row + dRow[i]
                    adjy = col + dCol[i]
                    if self.inBoard(adjx, adjy): 
                        st.append([adjx, adjy])
        
        dfs(self)

chars = [
    "a", "n", "c", "d",
    "e", "f", "g", "h",
    "i", "j", "k", "l",
    "m", "n", "o", "p"
]

new_board = Board(chars)
new_board.toString()

print(new_board.traverse())

    






