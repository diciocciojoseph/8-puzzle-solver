# Solves the 8-puzzle using BFS
# BFS provides an optimal solution
# The algorithm works by traversing nodes in order of their depth or level (how many moves have been applied)
# This ensures an optimal solution because of the level order traveral, we will never check deeper until all nodes
# of a current level have been explored

def BFS(puzzle):
    queue = [puzzle]                                # Initialize queue as python list
    visited = {}                                    # Initialize dictionary to keep track of visited states

    while(queue):                                                   
        cur = queue.pop(0)                          # Pop the current node (this will be a level above it's children)
        if cur.state == cur.solution:               # Check for solution
            cur.printSolution()
            return

        visited[str(cur.state)] = True              # Mark state as visited and expand children (apply poss. moves)
        children = cur.expand()

        for child in children:                      # Add children to queue if they have not already been explored
            if str(child.state) not in visited:
                queue.append(child) 

    print("No Solution")                            # All states exhausted - no solutions for given puzzle
