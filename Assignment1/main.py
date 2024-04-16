import sys

from utils import *
from classDef import *
from uninformedSearch import *
from informedSearch import *
from customSearch import *
from GUI import *

filename = sys.argv[1]
strategy = sys.argv[2]
# display = sys.argv[3]


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


def runRobotNav(init_pos, goal_pos, grid):
    problem = RobotNavProblem(init_pos, goal_pos, grid)
    if strategy == "BFS":
        result, nodenum = breadth_first_graph_search(problem)
    if strategy == "DFS":
        result, nodenum = depth_first_graph_search(problem)
    if strategy == "GBFS":
        result, nodenum = best_first_graph_search(
            problem, lambda n: problem.h(n))
    if strategy == "AStar":
        result, nodenum = astar_search(problem)
    if strategy == "IDS":
        result = iterative_deepening_search(problem)
    if strategy == "RBFS":
        result = recursive_best_first_search(problem)

    print(filename + " " + strategy)

    if result:
        if nodenum is not None:
            print(result, nodenum, sep=" ")
        else:
            print(result + " " + len(result.solution(0)))

        delta = {
            (0, -1): "UP",
            (0, 1): "DOWN",
            (-1, 0): "LEFT",
            (1, 0): "RIGHT"
        }

        path = [delta.get(action) for action in result.solution()]
        print(path)
    else:
        print("No goal is reachable " + len(result.solution()))

    print(problem.h(Node((7, 0))))


def main():
    parse_input_file(filename)

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

    runRobotNav(init_pos, goal_pos, grid)


if __name__ == "__main__":
    main()
