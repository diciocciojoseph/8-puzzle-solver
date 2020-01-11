import pqueue

# Solves the 8-puzzle using Uniform Cost Search (UCS)
# This algorithm provides an optimal solution
# This algorithm picks nodes to explore based on their cost to achieve a certain position
# Namely, their depth from the starting position (how many moves had to be made)
# Because of this, we will always reach the solved state with the lowest score (or depth) first,
# which explains it's optimality


def UCS(puzzle):
    
    puzzle.score = puzzle.depth                                 # Assign score to depth
    queue = pqueue.PriorityQueue(lambda node: node.depth)       # Initialize queue with depth as prio. func.
    queue.push(puzzle)                                          # Push initial puzzle state
    visited = {}                                                # Initialize visited dictionary to prevent dup. states

    while queue:
        cur = queue.pop()                                       # Visit the current node
        visited[str(cur.state)] = True
        if cur.state == cur.solution:
            cur.printSolution()
            return

        children = cur.expand()                                 # Expand children and score based on depth
        for child in children:                                  # Add them to the queue if unvisited
            child.score = child.depth                           # The queue will maintain depth priorty for poped node
            if str(child.state) not in visited:
                queue.push(child)
