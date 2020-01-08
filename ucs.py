import pqueue

# Solves the 8-puzzle using Uniform Cost Search (UCS)
# This algorithm picks nodes to explore based on their cost


def UCS(puzzle):
    
    puzzle.score = puzzle.depth
    queue = pqueue.PriorityQueue(lambda node: node.depth)
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
            child.score = child.depth
            if str(child.state) not in visited:
                queue.push(child)
