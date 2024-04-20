from utils import *


class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return (state in self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise NotImplementedError


class RobotNavProblem(Problem):
    def __init__(self, initial, goal, grid):
        super().__init__(initial, goal)
        self.grid = grid

    def actions(self, state):
        actions = []
        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:  # Actions: UP, LEFT, DOWN, RIGHT
            new_x, new_y = state[0] + dx, state[1] + dy
            # Check grid bounds and obstacles
            if 0 <= new_x < len(self.grid[0]) and 0 <= new_y < len(self.grid) and self.grid[new_y][new_x] != -1:
                actions.append((dx, dy))

        return actions

    def result(self, state, action):
        return (state[0] + action[0], state[1] + action[1])

    def goal_test(self, state):
        return super().goal_test(state)

    # Heuristic function to reach a goal
    def h(self, node):
        minn = float('inf')
        for goal in self.goal:
            minn = min(minn, manhattan_distance(node.state, goal))
        return minn

    def h_all_goals(self, node, visited_goals):
        current_state = node.state
        unvisited_goals = set(self.goal) - visited_goals

        minn = float('inf')
        for goal in unvisited_goals:
            minn = min(manhattan_distance(current_state, goal))
        return minn


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self)

    def child_node(self, problem, action):
        # Get the next tile
        next_state = problem.result(self.state, action)

        # initialize the next node in the search tree
        next_node = Node(next_state, self, action, problem.path_cost(
            self.path_cost, self.state, action, next_state))

        return next_node

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def solution(self):
        return [node.action for node in self.path()[1:]]
