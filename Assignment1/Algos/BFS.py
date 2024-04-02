import utils
from collections import deque


def breadth_first_tree_search(problem):
    frontier = deque([Node(problem.initial)])  # FIFO queue

    while frontier:
        node = frontier.popleft()

        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None
