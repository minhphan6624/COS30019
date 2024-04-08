import sys

from collections import deque

from utils import *


class Node:
    """Create a search tree Node, derived from a parent by an action."""
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
        return hash(self.state)

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(
            self.path_cost, self.state, action, next_state))
        return next_node
    
    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    """Return a list of nodes forming the path from the root to this node."""
    def path(self):    
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
    

class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise NotImplementedError


class RobotNavProblem(Problem):
    def __init__(self, initial, goal, walls, grid_h, grid_w):
        super().__init__(initial, goal)
        self.walls = walls
        self.grid_w = grid_w
        self.grid_h = grid_h
        self.curr_pos = self.initial

    def actions(self, state):
        possible_actions = ['UP', 'LEFT', 'DOWN', 'RIGHT']

        #Blocks on the left most cannot move further left
        if (self.curr_pos[0] == 0):
            possible_actions.remove('LEFT')

        #Blocks on the right most cannot move further right
        if (self.curr_pos[0] == self.grid_w - 1):
            possible_actions.remove('RIGHT')

        #Blocks at the top cannot move further up
        if (self.curr_pos[1] == 0):
            possible_actions.remove('UP')

        #Blocks at the bottom most cannot move further down
        if (self.curr_pos[1] == self.grid_h - 1):
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        x, y = self.curr_pos[0], self.curr_pos[1]
        if (action == "UP"):
            return (x, y+1)  
        elif (action == "DOWN"):
            return (x, y+1)  
        elif (action == "LEFT"):
            return (x-1, y)  
        elif (action == "RIGHT"):
            return (x+1, y)    
        
    def goal_test(self, state):
        return state == self.goal
