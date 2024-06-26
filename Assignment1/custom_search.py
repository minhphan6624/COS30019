import sys
import numpy as np

from class_def import *
from utils import *


def iterative_deepening_search(problem):
    explored_count = 0

    def depth_limited_search(problem, limit=50):

        def recursive_dls(node, problem, limit):
            nonlocal explored_count
            explored_count += 1

            if problem.goal_test(node.state):
                return node
            elif limit == 0:
                return 'cutoff'
            else:
                cutoff_occurred = False

                for child in node.expand(problem):
                    result = recursive_dls(child, problem, limit - 1)

                    if result == 'cutoff':
                        cutoff_occurred = True

                    # If there is a result
                    elif result is not None:
                        return result
                return 'cutoff' if cutoff_occurred else None

        # Body of depth_limited_search:
        return recursive_dls(Node(problem.initial), problem, limit)

    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            break

    return result, explored_count


def recursive_best_first_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    explored_count = 0

    def RBFS(problem, node, flimit, explored_count):
        explored_count += 1

        # Terminates if a goal is reached
        if problem.goal_test(node.state):
            return node, 0, explored_count  # (The second value is immaterial)

        successors = node.expand(problem)

        # Terminates if a node has no other child node
        if len(successors) == 0:
            return None, np.inf, explored_count

        for s in successors:
            s.f = max(s.path_cost + h(s), node.f)

        while True:
            # Order by lowest f value
            successors.sort(key=lambda x: x.f)

            best = successors[0]

            if best.f > flimit:
                return None, best.f, explored_count

            if len(successors) > 1:
                alternative = successors[1].f
            else:
                alternative = np.inf

            result, best.f, explored_count = RBFS(
                problem, best, min(flimit, alternative), explored_count)

            if result is not None:
                return result, best.f, explored_count

    # Body of RBFS
    node = Node(problem.initial)
    node.f = h(node)
    result, bestf, explored_count = RBFS(problem, node, np.inf, explored_count)
    return result, explored_count
