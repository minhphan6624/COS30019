import sys

from utils import *
from classDef import *
from uninformedSearch import *
from informedSearch import *

filename = sys.argv[1]
strategy = sys.argv[2]


def parse_input_file(filename):
    with open(filename, 'r') as f:
        # Read map size
        map_size = f.readline().strip().strip('[]').split(',')
        rows, cols = int(map_size[0]), int(map_size[1])

        # Read start position
        init_pos = f.readline().strip().strip('()').split(',')
        init_pos = (int(init_pos[0]), int(init_pos[1]))

        # Read goal positions
        goal_pos = f.readline().strip().split('|')
        goal_pos = [(int(pos.strip().strip("()").split(',')[0]), int(pos.strip().strip("()").split(',')[1]))
                    for pos in goal_pos]

        # Read walls
        walls = []  # Array of walls
        for line in f:
            parts = line.strip().strip("()").split(',')
            w, h = int(parts[2]), int(parts[3])

            x, y = int(parts[0]), int(parts[1])
            for i in range(0, w):
                for j in range(0, h):
                    wall_block = (x + i, y+j)

                    walls.append(wall_block)

        return rows, cols, init_pos, goal_pos, walls


rows, cols, init_pos, goal_pos, walls = parse_input_file(filename)

grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Marking starting position as 1
grid[init_pos[1]][init_pos[0]] = 1

# Marking goals as 2
for gx, gy in goal_pos:
    grid[gy][gx] = 2

# Marking walls as -1
for wx, wy in walls:
    grid[wy][wx] = -1


def print_grid(grid):
    for row in grid:
        print(row)


def runRobotNav():
    problem = RobotNavProblem(init_pos, goal_pos, grid)

    if strategy == "BFS":
        result = breadth_first_graph_search(problem)
    if strategy == "DFS":
        result = depth_first_graph_search(problem)
    if strategy == "GBFS":
        pass
    if strategy == "AStar":
        pass

    print(filename + " " + strategy)

    if result:
        print(result, len(result.solution()), sep=" ")

        delta = {
            (0, -1): "UP",
            (0, 1): "DOWN",
            (-1, 0): "LEFT",
            (1, 0): "RIGHT"
        }

        path = [delta.get(action) for action in result.solution()]
        print(path)
    else:
        print("No goal is reachable")


# Program execution
runRobotNav()
