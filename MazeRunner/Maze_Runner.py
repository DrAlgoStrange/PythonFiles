import tkinter as tk
import random

TILE_SIZE = 40

# Simple maze layout (1 = wall, 0 = path)
MAZE1 = [
    [[1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,1],
    [1,0,1,0,1,0,1,1],
    [1,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,0,1,0,1],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1]],
    [[1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,1],
    [1,0,1,0,1,0,1,1],
    [1,0,1,0,1,0,0,1],
    [1,0,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,0,1,0,1],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1]]
]
MAZE=random.choice(MAZE1)

PLAYER_COLOR = "blue"
EXIT_COLOR = "green"
WALL_COLOR = "black"
PATH_COLOR = "white"

class MazeEscape:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Escape")
        self.canvas = tk.Canvas(root, width=len(MAZE[0])*TILE_SIZE, height=len(MAZE)*TILE_SIZE)
        self.canvas.pack()
        self.player_pos = [1, 1]  # Start position
        self.exit_pos = [7, 7]    # Exit position

        self.draw_maze()
        self.draw_player()
        self.root.bind("<Key>", self.move_player)

    def draw_maze(self):
        for y, row in enumerate(MAZE):
            for x, cell in enumerate(row):
                color = WALL_COLOR if cell == 1 else PATH_COLOR
                if [y, x] == self.exit_pos:
                    color = EXIT_COLOR
                self.canvas.create_rectangle(
                    x*TILE_SIZE, y*TILE_SIZE, (x+1)*TILE_SIZE, (y+1)*TILE_SIZE,
                    fill=color, outline="gray"
                )

    def draw_player(self):
        x, y = self.player_pos[1], self.player_pos[0]
        self.player = self.canvas.create_oval(
            x*TILE_SIZE+5, y*TILE_SIZE+5,
            (x+1)*TILE_SIZE-5, (y+1)*TILE_SIZE-5,
            fill=PLAYER_COLOR
        )

    def move_player(self, event):
        dx, dy = 0, 0
        if event.keysym == "Up":
            dy = -1
        elif event.keysym == "Down":
            dy = 1
        elif event.keysym == "Left":
            dx = -1
        elif event.keysym == "Right":
            dx = 1

        new_y = self.player_pos[0] + dy
        new_x = self.player_pos[1] + dx

        if MAZE[new_y][new_x] == 0:
            self.player_pos = [new_y, new_x]
            self.canvas.delete(self.player)
            self.draw_player()

        if self.player_pos == self.exit_pos:
            self.canvas.create_text(
                TILE_SIZE*4, TILE_SIZE*4,
                text="YOU ESCAPED!", fill="red", font=("Arial", 24)
            )
            self.root.unbind("<Key>")

if __name__ == "__main__":
    root = tk.Tk()
    game = MazeEscape(root)
    root.mainloop()
