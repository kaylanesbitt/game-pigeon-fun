import tkinter as tk
from games.word_hunt import Board 

def main(): 
    chars = input("Enter your board: ")

    board = Board(chars)

    words = board.find_words()

    window = tk.Tk()
    window.title("Word Hunt")
    

    # Canvas below
    canvas = tk.Canvas(window, width=800, height=800, bg="white")
    canvas.grid(row=4, column=4)

    # Draw something on the canvas
    canvas.create_line(50, 50, 350, 350, fill="red", width=3)

    # Function to clear canvas
    def clear_canvas(event=None):
        canvas.delete("all")

    # Bind key commands
    window.bind("<Right>", clear_canvas)
    window.bind("<Escape>", lambda event: window.destroy())

    window.mainloop()

    

if __name__ == "__main__": 
    main()