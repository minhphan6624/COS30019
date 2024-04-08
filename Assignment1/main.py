import sys

from ClassDef import *
from BFS import *
from DFS import *

filename = sys.argv[1]
strategy = sys.argv[2]


def parse_input_file(filename):
    with open(filename, 'r') as f:
        # Read map size
        map_size = f.readline().strip().strip('[]').split(',')
        height, width = int(map_size[0]), int(map_size[1])

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
            w,h =  int(parts[2]), int(parts[3])

            x,y = int(parts[0]), int(parts[1])
            for i in range(0, w):
                for j in range(0, h):
                    wall_block = (x + i,y+j)

                    # If the block is the goal or already checked as a wall
                    # if (wall_block in goal_pos or wall_block in walls):
                    #     continue
                    # else:
                    walls.append(wall_block)
                

        return height, width, init_pos, goal_pos, walls


height, width, init_pos, goal_pos, walls = parse_input_file(filename)

def runRobotNav():
    #Initialize the problem
    problem = RobotNavProblem(initial = init_pos, goal = goal_pos, walls=walls, 
                              grid_h=height, grid_w = width)

    if strategy == "BFS":
        result = breadth_first_tree_search(problem)

        print(filename + " ")
        print(strategy + "\n")

        path = result.solution()
        
        print(result + " " + len(path))
        print(path)
        

    if strategy == "DFS":
        result = depth_first_tree_search(problem)

        print(filename + " ")
        print(strategy + "\n")

        path = result.solution()
        
        print(result + " " + len(path))
        print(path)
    if strategy == "G_BEST":
        print ("Greedy Best-First Search")
    if strategy == "A_STAR":
        print ("A* Search")

    

# print(f"Grid Size: {height}x{width}")
# print(f"Start Position: {init_pos}")
# print(f"Goal Positions: {goal_pos}")
# print(f"Walls: {walls}")
runRobotNav()