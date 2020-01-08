# BFS algorithm applied to 8-puzzle


def BFS(puzzle):
    # Initialize a queue for standard order-level traversal
    # And a map to keep track of all visited states (prevent duplicates)
    queue = [puzzle]
    visited = {}

    while(queue):
        cur = queue.pop(0)

        # If the current state is the solution, we are done
        if cur.state == cur.solution:
            cur.printSolution()
            return

        # Else, mark the state as visited (use stringified state as key), and append ALL child nodes to the queue
        visited[str(cur.state)] = True
        children = cur.expand()

        for child in children:
            if str(child.state) not in visited:
                queue.append(child)

    # If we ever exit the loop without finding a solution, the puzzle is unsolveable
    # In the future, I may implement a check to determine this beforehand (check tile inversions)
    print("All States Exhausted: No Solution Found")
