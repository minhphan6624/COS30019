import sys
import numpy as np

from classDef import *
from utils import *


def iterative_deepening_search(problem):
    nodenum = 0

    def depth_limited_search(problem, limit=50):

        def recursive_dls(node, problem, limit):
            nonlocal nodenum
            nodenum += 1

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

    return result, nodenum


def recursive_best_first_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    nodenum = 0

    def RBFS(problem, node, flimit, nodenum):
        nodenum += 1

        # Terminates if a goal is reached
        if problem.goal_test(node.state):
            return node, 0, nodenum  # (The second value is immaterial)

        successors = node.expand(problem)

        # Terminates if a node has no other child node
        if len(successors) == 0:
            return None, np.inf, nodenum

        for s in successors:
            s.f = max(s.path_cost + h(s), node.f)

        while True:
            # Order by lowest f value
            successors.sort(key=lambda x: x.f)

            best = successors[0]

            if best.f > flimit:
                return None, best.f, nodenum

            if len(successors) > 1:
                alternative = successors[1].f
            else:
                alternative = np.inf

            result, best.f, nodenum = RBFS(
                problem, best, min(flimit, alternative), nodenum)

            if result is not None:
                return result, best.f, nodenum

    # Body of RBFS
    node = Node(problem.initial)
    node.f = h(node)
    result, bestf, nodenum = RBFS(problem, node, np.inf, nodenum)
    return result, nodenum
