from classDef import *
from collections import deque


def breadth_first_graph_search(problem):
    start = Node(problem.initial)  # Root node points to the start position
    nodenum = 1

    # Check whether the agent starts at a goal state
    if problem.goal_test(start.state):
        return start, nodenum

    # Set up the frontier as a queue and a set to keep track of explored nodes
    frontier = deque([start])
    explored = set()

    while frontier:
        print(frontier)
        node = frontier.popleft()
        explored.add(node.state)

        if problem.goal_test(node.state):  # Terminate if a goal is reached
            return node, nodenum

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                # if problem.goal_test(child.state):
                #     return child, nodenum + 1
                frontier.append(child)
                nodenum += 1
    return None, nodenum


def depth_first_graph_search(problem):
    start = Node(problem.initial)  # Root node points to the start position
    nodenum = 1

    frontier = [(start)]  # Stack
    explored = set()

    if problem.goal_test(start.state):  # Check if the agent starts at a goal state
        return start, nodenum

    while frontier:
        print(frontier)
        node = frontier.pop()
        explored.add(node.state)

        if problem.goal_test(node.state):  # Terminate if a goal is reached
            return node, nodenum+1

        for child in node.expand(problem):  # Explore the child nodes
            if child.state not in explored and child not in frontier:
                frontier.append(child)
                nodenum += 1

    return None, nodenum


def bfs_all_goals(problem):
    start = Node(problem.initial)
    nodenum = 1

    visited_goals = set()  # Track visited goals
    all_goals = set(problem.goal)  # All target goals
    final_paths = []  # Store the final concatenated path

    if problem.goal_test(start.state):  # Check if the agent starts at a goal position
        visited_goals.add(start.state)
        final_paths = start.solution()

    # Set up the frontier as a queue and a set to keep track of explored nodes
    frontier = deque([start])
    explored = set()

    while frontier and visited_goals != all_goals:
        print(frontier)
        node = frontier.popleft()
        explored.add(node.state)

        if problem.goal_test(node.state) and node.state not in visited_goals:
            visited_goals.add(node.state)
            final_paths = node.solution()

            # Reset the search from the current goal
            frontier.clear()
            explored.clear()
            start = Node(node.state)  # New start node from current goal
            frontier.append(start)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                # if problem.goal_test(child.state) and child.state not in visited_goals:
                #     visited_goals.add(child.state)
                #     final_paths = child.solution()
                frontier.append(child)
                nodenum += 1

    # Return the full path through all goals and the number of nodes explored
    return final_paths, nodenum


def dfs_all_goals(problem):

    start = Node(problem.initial)  # Root node points to the start position
    nodenum = 1

    visited_goals = set()  # To keep track of all visited goals
    all_goals = set(problem.goal)
    final_paths = []  # Store the final concatenated path

    if problem.goal_test(start.state):  # Check if the agent starts at a goal position
        visited_goals.add(start.state)
        final_paths = start.solution()

    frontier = [(start)]  # Stack
    explored = set()

    while frontier and visited_goals != all_goals:
        node = frontier.pop()
        explored.add(node.state)

        if problem.goal_test(node.state) and node.state not in visited_goals:
            visited_goals.add(node.state)
            final_paths = node.solution()

        # Reset the search from the current goal
            frontier.clear()
            explored.clear()
            start = Node(node.state)  # New start node from current goal
            frontier.append(start)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
                nodenum += 1

    return final_paths, nodenum  # Return None if not all goals can be reached
