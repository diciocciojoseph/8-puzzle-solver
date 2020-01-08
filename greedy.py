import pqueue
import heuristics

# Solves the 8-puzzle using greedy search
# This search simply uses a heuristic value (hamming/manhattan) to choose which child to expand
# This algorithm does not guarentee an optimal solution, and does not backtrack (only a single chain will be explored)


def GREEDY(puzzle, heuristic=heuristics.hamming):
    puzzle.score = heuristic(puzzle)
    queue = pqueue.PriorityQueue(heuristic)
    queue.push(puzzle)
    visited = {}

    while queue:
        cur = queue.pop()
        visited[str(cur.state)] = True
        if cur.state == cur.solution:
            cur.printSolution()
            return

        children = cur.expand()
        for child in children:
            child.score = heuristic(child)
            if str(child.state) not in visited:
                queue.push(child)
