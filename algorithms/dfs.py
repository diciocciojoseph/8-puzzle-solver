# Solves the 8-puzzle using DFS
# This algorithm does not provide an optimal solution
# The dfs algorithm "randomly" picks a generated child state, it does not use any score or heuristic
# an optimal solution is not given because we many traverse deep through many states before reaching the solution
# in an arbitrary order

def DFS(puzzle):
    stack = []                                          # Initialize stack for depth-traverse, start with given puzzle
    visited = {}                                        # Keep track of visited states

    stack.append(puzzle)                            

    while stack:
        cur = stack.pop()                               # Pop the current node/state and visit it
        visited[str(cur.state)] = True
        if cur.state == cur.solution:
            cur.printSolution()
            return
        else:
            children = cur.expand()                     # Add all non-visited children to the stack
            for child in children:
                if str(child.state) not in visited:
                    stack.append(child)

    print("No Solution")