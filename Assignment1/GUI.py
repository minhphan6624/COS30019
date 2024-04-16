import tkinter as tk


class RobotNavApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Robot Navigation")
        self.geometry("920x700")  # Adjust the size as needed

        # self.grid = grid

        self.label = tk.Label(self, text="A simple label", font=("Arial", 11))
        self.label.pack()

        # self.grid_display = GridDisplay(
        #     self, len(self.grid[0]), len(self.grid))  # 10x10 grid for example
        self.grid_display = GridDisplay(self, 10, 10)
        self.grid_display.pack()

        self.control_panel = ControlPanel(self)
        self.control_panel.pack()

    def update_gui(self, node, status):
        x, y = node.position
        color = {"visited": "gray", "current": "blue", "goal": "green"}[status]
        self.grid_display.update_cell(x, y, color)


class GridDisplay(tk.Canvas):
    def __init__(self, parent, rows, cols, size=50):
        super().__init__(parent, bg='white', height=rows*size, width=cols*size)
        self.rows = rows
        self.cols = cols
        self.size = size
        self.draw_grid()

    def draw_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.create_rectangle(j*self.size, i*self.size,
                                      (j+1)*self.size, (i+1)*self.size, fill='white')

    def update_cell(self, x, y, color):
        self.create_rectangle(x*self.size, y*self.size,
                              (x+1)*self.size, (y+1)*self.size, fill=color)
        self.update()


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
