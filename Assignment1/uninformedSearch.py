from classDef import *
from collections import deque


def breadth_first_graph_search(problem):
    start = Node(problem.initial)  # Root node points to the start position
    nodenum = 1

    if problem.goal_test(start.state):
        return start, nodenum

    frontier = deque([start])
    explored = set()

    while frontier:
        print(frontier)
        # Set up the frontier as a queue and the list of explored nodes as a set
        node = frontier.popleft()
        explored.add(node.state)

        if problem.goal_test(node.state):
            return node, nodenum

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child, nodenum + 1
                frontier.append(child)
                nodenum += 1
    return None, nodenum


def depth_first_graph_search(problem):
    start = Node(problem.initial)  # Root node points to the start position
    nodenum = 1

    frontier = [(start)]  # Stack
    explored = set()

    if problem.goal_test(start.state):
        return start, nodenum

    while frontier:
        node = frontier.pop()
        explored.add(node.state)

        if problem.goal_test(node.state):
            return node, nodenum+1

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:

                if problem.goal_test(child.state):
                    return child, nodenum + 1

                frontier.append(child)
                nodenum += 1

    return None, nodenum


def bfs_all_goals(problem):

    start = Node(problem.initial)  # Root node points to the start position
    nodenum = 1

    visited_goals = set()  # To keep track of all visited goals
    all_goals = set(problem.goal)

    final_paths = []  # Store the path to the lastest goal
    current_goal_path = []

    if problem.goal_test(start.state):
        visited_goals.add(start.state)
        final_path = start.path()

    frontier = deque([start])
    explored = set()

    while frontier and visited_goals != all_goals:
        node = frontier.popleft()
        explored.add(node.state)

        if problem.goal_test(node.state):
            # visited_goals.add(node.state)
            # if node.state not in goal_paths:  # Capture path if not already captured
            #     goal_paths[node.state] = node.solution()
            # if visited_goals == all_goals:
            #     # Return the last goal reached, the path and number of nodes explored
            #     return node, goal_paths, nodenum
            visited_goals.add(node.state)
            current_goal_path = node.solution()
            # Concatenate path to current goal
            final_paths.extend(current_goal_path)

            # Reset the search from the current goal
            frontier.clear()
            explored.clear()
            start = Node(node.state)  # New start node from current goal
            frontier.append(start)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:

                if problem.goal_test(child.state):
                    visited_goals.add(child.state)
                    if child.state not in goal_paths:  # Capture path if not already captured
                        goal_paths[child.state] = child.solution()
                    if visited_goals == all_goals:
                        return node, goal_paths, nodenum

                frontier.append(child)
                nodenum += 1

    # Return paths or None if not all goals can be reached
    return None, goal_paths if goal_paths else None, nodenum


def dfs_all_goals(problem):

    node = Node(problem.initial)  # Root node points to the start position
    nodenum = 1

    visited_goals = set()  # To keep track of all visited goals
    all_goals = set(problem.goal)

    if problem.goal_test(node.state):
        visited_goals.add(node.state)

    frontier = [(node)]  # Stack
    explored = set()

    while frontier and visited_goals != all_goals:
        node = frontier.pop()
        explored.add(node.state)

        if problem.goal_test(node.state):
            visited_goals.add(node.state)
            if visited_goals == all_goals:
                return node, nodenum  # Return the last goal reached and number of nodes explored

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:

                if problem.goal_test(child.state):
                    visited_goals.add(child.state)

                    if visited_goals == all_goals:
                        return child, nodenum  # Return the last goal reached and number of nodes explored

                frontier.append(child)
                nodenum += 1

    return None, nodenum  # Return None if not all goals can be reached
