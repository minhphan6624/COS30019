from classDef import *
from collections import deque


def breadth_first_graph_search(problem):
    node = Node(problem.initial)

    if problem.goal_test(node.state):
        return node

    frontier = deque([node])
    explored = set()

    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None


def depth_first_graph_search(problem):
    frontier = [(Node(problem.initial))]  # Stack
    explored = set()

    while frontier:
        node = frontier.pop()

        if problem.goal_test(node.state):
            return node

        explored.add(node.state)

        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)
    return None
