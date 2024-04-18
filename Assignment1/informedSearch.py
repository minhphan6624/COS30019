from utils import *
import heapq
from classDef import *
from collections import deque


def best_first_graph_search(problem, f, display=False):

    # f(x) will be cached on the nodes as they are computed
    f = memoize(f, 'f')

    start = Node(problem.initial)
    nodenum = 1

    if problem.goal_test(start.state):
        return start, nodenum

    frontier = PriorityQueue('min', f)
    frontier.append(start)
    explored = set()

    while frontier:
        # print(frontier, end=" popped ")

        node = frontier.pop()

        # print(node)

        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and",
                      len(frontier), "paths remain in the frontier")
            return node, nodenum+1

        explored.add(node.state)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child, nodenum + 1
                frontier.append(child)
                nodenum += 1
            elif child in frontier:
                # Reorder the child in the queue if its current f(x) value is smaller than the f(x) value stored in frontier
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None, nodenum


def astar_search(problem, h=None, display=False):
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)
