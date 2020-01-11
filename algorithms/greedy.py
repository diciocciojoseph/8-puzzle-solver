import pqueue
import heuristics

# Solves the 8-puzzle using greedy search
# This algorithm does not guarentee an optimal solution
# This search simply uses a heuristic value (hamming/manhattan) to choose which child to expand
# By always picking the node closest to being solved, we reach the solution fairly quickly, but sub-optimally
# in terms of moves made

def GREEDY(puzzle, heuristic=heuristics.hamming):
    puzzle.score = heuristic(puzzle)                    # Set initial score using heuristic
    queue = pqueue.PriorityQueue(heuristic)             # Initialize queue with given heuristic for priority
    queue.push(puzzle)                                  # Add first puzzle to queue
    visited = {}                                        # Initialize dictionary to keep track of visited states

    while queue:                                        
        cur = queue.pop()                               # Pop the item with the best heuristic score (located at front)
        visited[str(cur.state)] = True                  # Mark current state as visiteed
        if cur.state == cur.solution:                   # Check for solution, if so exit
            cur.printSolution()
            return

        children = cur.expand()                         # Expand the current node, assign scores, and push to queue
        for child in children:                          # the queue will maintain the best puzzle at the top to be poped
            child.score = heuristic(child)
            if str(child.state) not in visited:
                queue.push(child)

    print("No Solution")                                # No solution found (puzzle insolvable)