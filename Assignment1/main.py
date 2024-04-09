import sys

from utils import *
from classDef import *
from uninformedSearch import *
from informedSearch import *

filename = sys.argv[1]
# strategy = sys.argv[2]


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

grid[init_pos[1]][init_pos[0]] = 1

for gx, gy in goal_pos:
    grid[gy][gx] = 2

for wx, wy in walls:
    grid[wy][wx] = -1


def print_grid(grid):
    for row in grid:
        print(row)


def runRobotNav():
    problem = RobotNavProblem(init_pos, goal_pos, grid)

    result = depth_first_graph_search(problem)
    # result = breadth_first_graph_search(problem)
    # result = best_first_graph_search(problem)

    delta = {
        (0, -1): "UP",
        (0, 1): "DOWN",
        (-1, 0): "LEFT",
        (1, 0): "RIGHT"
    }
    path = []
    pNode = result
    while pNode.parent:
        path.insert(0, delta.get(pNode.action))
        pNode = pNode.parent
    print(path)


# Program execution
runRobotNav()
