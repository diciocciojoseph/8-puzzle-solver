import heapq

# A* algorithm applied to 8-puzzle
# The A* algorithm gives each state a score f = g + h where
# g = is the movement cost (number of moves to reach the state, in this case it is the depth of the puzzle)
# h = is the estimated movement cost / heuristic (we can use manhattan distance or misplaced tile to get h)

# We then choose to traverse the node with the lowest f score, which hopefully results in the least-cost path
# At any point, we keep an open and closed list
# the open list keeps nodes we have yet to explore (starts with initial state)
# the close list keeps nodes we have explored
# we check both these lists before appending a child node (we don't want to re-calculate the same state)


# Manhattan Distance Priority Heuristic, where h total distance of tiles away from their solve positions


def fscore_manhattan(puzzle):
    pass


# Hamming Priority Heuristic, where h is the # of misplaced tiles (not counting blank space)


def fscore_hamming(puzzle):
    g = puzzle.depth
    h = 0            

    for i in range(len(puzzle.state)):
        if puzzle.state[i] != puzzle.solution[i] and puzzle.state[i] != 0:
            h += 1

    return h + g 


# Puzzle Heap
class PuzzleHeap:
    def __init__(self, initial=None, key=fscore_hamming):
        self.key = key
        self.data = []

    def push(self, item):
        heapq.heappush(self.data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self.data)[1]

# puzzle = puzzle to be solved
# score_func = score function (can used manhattan or hamming priorities if desired)


def A_STAR(puzzle, score_func=fscore_hamming):
    puzzle.score = score_func(puzzle)
    heap = PuzzleHeap(score_func)
    heap.push(puzzle)
    visited = {}

    while heap:
        cur = heap.pop()
        visited[str(cur.state)] = True
        if cur.state == cur.solution:
            cur.printSolution()
            return
        
        children = cur.expand()
        for child in children:
            child.score = score_func(child)
            if str(child.state) not in visited:
                heap.push(child)
    
