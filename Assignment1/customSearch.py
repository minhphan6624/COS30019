import sys

from classDef import *
from utils import *

# def dbsearch(problem, node, bound):
#     if problem.goal_test(node.state):
#         return node  # Return the node if goal is found
#     elif bound == 0:
#         return "cutoff"  # Terminates if node is at depth bound
#     elif bound > 0:
#         cutoff_occurred = False
#         for child in node.expand(problem):

#             result = dbsearch(problem, child, bound - 1)

#             if result == "cutoff":
#                 cutoff_occurred == True
#             elif result is not None:
#                 return result
#         return ("cutoff" if cutoff_occurred else None)


# def iterative_deepening_search(problem):
#     bound = 0
#     root = problem.initial

#     while True:
#         result = dbsearch(problem, Node(problem.initial), bound)

#         if result != 'cutoff':
#             return result

#         bound += 1

def depth_limited_search(problem, limit=50):
    """[Figure 3.17]"""

    def recursive_dls(node, problem, limit):
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
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    # Body of depth_limited_search:
    return recursive_dls(Node(problem.initial), problem, limit)


def iterative_deepening_search(problem):
    """[Figure 3.18]"""
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result


def recursive_best_first_search(problem, h=None):
    """[Figure 3.26]"""
    h = memoize(h or problem.h, 'h')

    def RBFS(problem, node, flimit):
        if problem.goal_test(node.state):
            return node, 0  # (The second value is immaterial)
        successors = node.expand(problem)
        if len(successors) == 0:
            return None, np.inf
        for s in successors:
            s.f = max(s.path_cost + h(s), node.f)
        while True:
            # Order by lowest f value
            successors.sort(key=lambda x: x.f)
            best = successors[0]
            if best.f > flimit:
                return None, best.f
            if len(successors) > 1:
                alternative = successors[1].f
            else:
                alternative = np.inf
            result, best.f = RBFS(problem, best, min(flimit, alternative))
            if result is not None:
                return result, best.f

    node = Node(problem.initial)
    node.f = h(node)
    result, bestf = RBFS(problem, node, np.inf)
    return result
