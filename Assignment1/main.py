import sys

from utils import *
from classDef import *
from uninformedSearch import *
from informedSearch import *
from customSearch import *
from GUI import *

filename = sys.argv[1]
strategy = sys.argv[2]
if len(sys.argv) == 4:
    all_goals = sys.argv[3]
else:
    all_goals = None


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
            x, y = int(parts[0]), int(parts[1])
            w, h = int(parts[2]), int(parts[3])

            for i in range(0, w):
                for j in range(0, h):
                    wall_block = (x + i, y+j)

                    walls.append(wall_block)

        return rows, cols, init_pos, goal_pos, walls


def runRobotNav(init_pos, goal_pos, grid):

    problem = RobotNavProblem(init_pos, goal_pos, grid)

    if strategy == "BFS":
        result, nodenum = breadth_first_graph_search(problem)
    elif strategy == "DFS":
        result, nodenum = depth_first_graph_search(problem)
    elif strategy == "GBFS":
        result, nodenum = best_first_graph_search(
            problem, lambda n: problem.h(n))
    elif strategy == "AStar":
        result, nodenum = astar_search(problem)
    elif strategy == "IDS":
        result, nodenum = iterative_deepening_search(problem)
    elif strategy == "RBFS":
        result = recursive_best_first_search(problem)
    else:
        print("Invalid Strategy")
        return

    print(filename + " " + strategy)

    if result:
        if nodenum:
            print(result, nodenum, sep=" ")

            # Print the path to the solution
            delta = {
                (0, -1): "UP",
                (0, 1): "DOWN",
                (-1, 0): "LEFT",
                (1, 0): "RIGHT"
            }

            path = [delta.get(action) for action in result.solution()]
            print(path)
        else:
            print(result)

            # Print the path to the solution
            delta = {
                (0, -1): "UP",
                (0, 1): "DOWN",
                (-1, 0): "LEFT",
                (1, 0): "RIGHT"
            }

            path = [delta.get(action) for action in result.solution()]
            print(path)
    else:
        print("No goal is reachable", nodenum)


def testing(init_pos, goal_pos, grid):
    problem = RobotNavProblem(init_pos, goal_pos, grid)
    if strategy == "BFS":
        path, nodenum = bfs_all_goals(problem)
    elif strategy == "DFS":
        path, nodenum = dfs_all_goals(problem)

    delta = {
        (0, -1): "UP",
        (0, 1): "DOWN",
        (-1, 0): "LEFT",
        (1, 0): "RIGHT"
    }

    path = [delta.get(action) for action in path]
    print(path)
    print(nodenum)


def main():
    rows, cols, init_pos, goal_pos, walls = parse_input_file(filename)

    # initialize the grid
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Marking starting position as 1
    grid[init_pos[1]][init_pos[0]] = 1

    # Marking goals as 2
    for gx, gy in goal_pos:
        grid[gy][gx] = 2

    # Marking walls as -1
    for wx, wy in walls:
        grid[wy][wx] = -1

    # for row in grid:
    #     print(row)

    if all_goals:
        testing(init_pos, goal_pos, grid)
    else:
        runRobotNav(init_pos, goal_pos, grid)


if __name__ == "__main__":
    main()
