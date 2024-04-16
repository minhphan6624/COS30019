from classDef import *
from collections import deque


def breadth_first_graph_search(problem):
    node = Node(problem.initial)  # Root node points to the start position
    nodenum = 1

    if problem.goal_test(node.state):
        return node, nodenum

    frontier = deque([node])
    explored = set()

    while frontier:
        print(frontier)
        node = frontier.popleft()
        explored.add(node.state)

        if problem.goal_test(node.state):
            return node, nodenum
        # Set up the frontier as a queue and the list of explored nodes as a set

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child, nodenum + 1
                frontier.append(child)
                nodenum += 1
    return None, nodenum


def depth_first_graph_search(problem):
    node = Node(problem.initial)  # Root node points to the start position
    nodenum = 1

    frontier = [(node)]  # Stack
    explored = set()

    while frontier:

        print(frontier)
        node = frontier.pop()

        if problem.goal_test(node.state):
            return node, nodenum+1

        explored.add(node.state)

        # frontier.extend(child for child in node.expand(problem)
        #                 if child.state not in explored and child not in frontier)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:

                if problem.goal_test(child.state):
                    return child, nodenum + 1

                # print(child.state)
                frontier.append(child)
                nodenum += 1

    return None, nodenum
