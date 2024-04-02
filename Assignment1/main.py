import sys

from ClassDef import *

filename = sys.argv[1]
# strategy = sys.argv[2]


def parse_input_file(filename):
    with open(filename, 'r') as f:
        # Read map size
        map_size = f.readline().strip().strip('[]').split(',')
        m, n = int(map_size[0]), int(map_size[1])

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
            walls.append((int(parts[0]), int(parts[1]),
                         int(parts[2]), int(parts[3])))

        return m, n, init_pos, goal_pos, walls


m, n, start_pos, goal_pos, walls = parse_input_file(filename)

def runRobotNav():
    #Initialize the problem
    problem = RobotNavProblem(initial = start_pos, goal = goal_pos)




print(f"Grid Size: {m}x{n}")
print(f"Start Position: {start_pos}")
print(f"Goal Positions: {goal_pos}")
print(f"Walls: {walls}")
