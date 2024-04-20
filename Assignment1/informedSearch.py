from utils import *
import heapq
from classDef import *
from collections import deque


def best_first_graph_search(problem, f):

    # f(x) will be cached on the nodes as they are computed
    f = memoize(f, 'f')

    start = Node(problem.initial)
    nodenum = 1

    # Check if the robot starts at a goal cell
    if problem.goal_test(start.state):
        return start, nodenum

    # Set up the frontier
    frontier = PriorityQueue('min', f)
    frontier.append(start)
    explored = set()

    while frontier:
        print(frontier, end=" popped ")

        # Examine the node with the lowest f(x) first
        node = frontier.pop()
        explored.add(node.state)

        print(node)

        # Terminates if a goal is reached
        if problem.goal_test(node.state):
            return node, nodenum

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                # If the child node is a goal, terminates
                # if problem.goal_test(child.state):
                #     return child, nodenum + 1

                # Otherwise add the child node to frontier
                frontier.append(child)
                nodenum += 1
            elif child in frontier:
                # Reorder the child in the queue if its current f(x) value is smaller than the f(x) value stored in frontier
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None, nodenum


def astar_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))


def gbfs_all_goals(problem, f=None):
    start = Node(problem.initial)
    nodenum = 1

    visited_goals = set()  # Visited goals
    all_goals = set(problem.goal)  # All target goals
    final_paths = []  # Store the final concatenated path

    # f(x) will be cached on the nodes as they are compute
    if f == None:
        f = memoize(lambda n: problem.h_all_goals(n, visited_goals), 'f')
    else:
        f = memoize(lambda n: n.path_cost +
                    problem.h_all_goals(n, visited_goals), 'f')

    # Set up the frontier as a priority queue based on the evaluation funciton
    frontier = PriorityQueue('min', f)
    frontier.append(start)
    explored = set()  # Track visited nodes

    # Check if the agent starts at a goal position
    if problem.goal_test(start.state):
        visited_goals.add(start.state)
        final_paths = start.solution()

    while frontier and visited_goals != all_goals:
        print(frontier, " popped", end=" ")
        node = frontier.pop()

        print(node)
        explored.add(node.state)

        # Mark the goal as visited
        if problem.goal_test(node.state) and node.state not in visited_goals:
            visited_goals.add(node.state)
            final_paths = node.solution()

            # Reset the search from the current goal
            frontier = PriorityQueue('min', f)
            explored.clear()
            start = Node(node.state)  # New start node from current goal
            frontier.append(start)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
                nodenum += 1
            elif child in frontier:
                # Reorder the child in the queue if its current f(x) value is smaller than the f(x) value stored in frontier
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return visited_goals, final_paths, nodenum


def astar_all_goals(problem, h=None):
    # h = memoize(h or problem.h_all_goals, 'h')
    return gbfs_all_goals(problem, lambda n: n.path_cost + problem.h_all_goals(n))
