import pqueue
import heuristics

# A* algorithm applied to 8-puzzle
# The A* algorithm gives each state a score f = g + h where
# g = is the movement cost (number of moves to reach the state, in this case it is the depth of the puzzle)
# h = is the estimated movement cost / heuristic (we can use manhattan distance or misplaced tile to get h)

# We then choose to traverse the node with the lowest f score, which hopefully results in the least-cost path
# At any point, we keep an open and closed list
# the open list keeps nodes we have yet to explore (starts with initial state)
# the close list keeps nodes we have explored
# we check both these lists before appending a child node (we don't want to re-calculate the same state)


# Uses Manhattan Distance Priority Heuristic, where h total distance of tiles away from their solve positions


def fscore_manhattan(puzzle):
    g = puzzle.depth
    h = heuristics.manhattan(puzzle)

    return h + g


# Uses Hamming Priority Heuristic, where h is the # of misplaced tiles (not counting blank space)


def fscore_hamming(puzzle):
    g = puzzle.depth
    h = heuristics.hamming(puzzle)

    return h + g


# puzzle = puzzle to be solved
# score_func = score function (can used manhattan or hamming priorities if desired)


def A_STAR(puzzle, score_func=fscore_hamming):
    puzzle.score = score_func(puzzle)
    queue = pqueue.PriorityQueue(score_func)
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
            child.score = score_func(child)
            if str(child.state) not in visited:
                queue.push(child)
