import tkinter as tk

from uninformedSearch import *


class RobotNavApp(tk.Tk):
    def __init__(self, grid):
        super().__init__()

        self.title("Robot Navigation")
        self.geometry("920x700")  # Adjust the size as needed
        self.grid = grid

        self.grid_display = GridDisplay(
            self, len(self.grid), len(self.grid[0]), grid)
        self.grid_display.pack()

        self.control_panel = ControlPanel(self)
        self.control_panel.pack()

    def update_gui(self, node, status):
        x, y = node.position
        color = {"visited": "gray", "current": "blue", "goal": "green"}[status]
        self.grid_display.update_cell(x, y, color)


class GridDisplay(tk.Canvas):
    def __init__(self, parent, rows, cols, grid, size=50):
        super().__init__(parent, bg='white', height=rows*size, width=cols*size)
        self.rows = rows
        self.cols = cols
        self.size = size
        self.grid = grid
        self.draw_init_grid()

    def draw_init_grid(self):
        for y in range(self.rows):
            for x in range(self.cols):
                cell_color = 'white'  # Default color for empty cells
                if self.grid[y][x] == -1:
                    cell_color = 'grey'  # Wall cells
                elif self.grid[y][x] == 1:
                    cell_color = 'red'  # Start positions
                elif self.grid[y][x] == 2:
                    cell_color = 'green'  # Goal positions

                self.create_rectangle(x*self.size, y*self.size,
                                      (x+1)*self.size, (y+1)*self.size, fill=cell_color, outline='black')

    def update_cell(self, x, y, color):
        # self.create_rectangle(x*self.size, y*self.size,
        #                       (x+1)*self.size, (y+1)*self.size, fill=color)
        # self.update()
        self.itemconfig(self.find_closest(
            (x + 0.5) * self.size, (y + 0.5) * self.size)[0], fill=color)


class ControlPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.start_button = tk.Button(
            self, text="Start", command=self.on_start)
        self.start_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(
            self, text="Reset", command=self.on_reset)
        self.reset_button.pack(side=tk.LEFT)

    def on_start(self):
        print("Start the search algorithm")

    def on_reset(self):
        print("Reset the search and clear the grid")
