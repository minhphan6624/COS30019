import sys

from utils import *
from class_def import *
from uninformed_search import *
from informed_search import *
from custom_search import *

filename = sys.argv[1]
strategy = sys.argv[2].lower()
if len(sys.argv) == 4:
    all_goals = sys.argv[3]
else:
    all_goals = None

# Read file input


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

    if strategy == "bfs":
        result, explored_count = breadth_first_graph_search(problem)
    elif strategy == "dfs":
        result, explored_count = depth_first_graph_search(problem)
    elif strategy == "gbfs":
        result, explored_count = best_first_graph_search(
            problem, lambda n: problem.h(n))
    elif strategy == "astar":
        result, explored_count = astar_search(problem)
    elif strategy == "ids":
        result, explored_count = iterative_deepening_search(problem)
    elif strategy == "rbfs":
        result, explored_count = recursive_best_first_search(problem)
    else:
        print("Invalid Strategy")
        return

    print(filename + " " + strategy)

    if result:
        print(result, explored_count, sep=" ")

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
        print("No goal is reachable", explored_count)


def runRobotNavAllGoals(init_pos, goal_pos, grid):
    problem = RobotNavProblem(init_pos, goal_pos, grid)
    if strategy == "bfs":
        goals, path, explored_count = bfs_all_goals(problem)
    elif strategy == "dfs":
        goals, path, explored_count = dfs_all_goals(problem)
    elif strategy == "gbfs":
        goals, path, explored_count = gbfs_all_goals(problem)
    elif strategy == "astar":
        goals, path, explored_count = astar_all_goals(problem)
    else:
        print("Invalid Strategy")
        return

    print(filename + " " + strategy)

    print(goals, " ", explored_count)

    delta = {
        (0, -1): "UP",
        (0, 1): "DOWN",
        (-1, 0): "LEFT",
        (1, 0): "RIGHT"
    }

    path = [delta.get(action) for action in path]
    print(path)
    print(len(path))


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

    if all_goals == "all_goals":
        runRobotNavAllGoals(init_pos, goal_pos, grid)
    else:
        runRobotNav(init_pos, goal_pos, grid)


if __name__ == "__main__":
    main()
