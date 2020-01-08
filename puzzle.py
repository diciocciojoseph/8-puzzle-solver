# Class definition for a puzzle, stores the state of the current puzzle
# self.state = list representation of 8-puzzle                        [ 1, 2, 3
# for example, the puzzle [1, 2, 3, 4, 5, 6, 7, 8, 0] represents - >    4, 5, 6
#                                                                       7, 8, 0 ]
# Where 0 is the blank space
# 
# self.depth = the depth of the current node (initialized to 0)
# self.prev = link to parent puzzle node (initialized to None), this assists with printing the solution chain
# self.score = score we will use to assign heuristic value for informed-searches if needed
# self.solution = puzzle solution state

class Puzzle:
    # Initialize the puzzle
    def __init__(self, state, depth=0, prev=None):
        self.state = state
        self.depth = depth
        self.prev = prev
        self.score = 0
        self.solution = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    # These functions are so if we compare puzzle objects with >, <, =, they are compared by score
    def __eq__(self, value):
        return self.score == value.score

    def __gt__(self, value):
        return self.score > value.score

    def __lt__(self, value):
        return self.score < value.score

    # Return child instances of puzzle
    # Any valid moves that could be made are calculated, 
    # then applied to the current state to create new Puzzle objects
    # The depth and prev link are also set
    def expand(self):
        blank_idx = self.state.index(0)

        # Possible moves exist in all adjancent tiles (row above/below, col to the left and right)
        # To validate moves we can simply check if 0 <= i <= 8
        # However, we also have cases where if i is on the right edge, we cannot go to i+1 (wraps around to other end)
        # or i-1 on the left edge (same reason)
        #
        # 0    i-3  0
        # i-1   i   i+1
        # 0    i+3  0

        possibleMoves = []

        # Move up/down
        possibleMoves.append(blank_idx - 3)
        possibleMoves.append(blank_idx + 3)

        # Move right/left (if valid)
        if blank_idx != 2 and blank_idx != 5:
            possibleMoves.append(blank_idx + 1)
        if blank_idx != 3 and blank_idx != 6:
            possibleMoves.append(blank_idx-1)

        # Filter array bounds
        validMoves = []
        for x in possibleMoves:
            if x >= 0 and x <= 8:
                validMoves.append(x)

        # Create child puzzles with moves applied and fields updated
        children = []
        for idx in validMoves:
            new_state = self.state[:]
            new_state[blank_idx], new_state[idx] = new_state[idx], new_state[blank_idx]
            children.append(Puzzle(new_state, self.depth + 1, self))

        return children

    # Print this puzzle
    def printPuzzle(self):
        print("*********************")
        r1 = self.state[:3]
        r2 = self.state[3:6]
        r3 = self.state[6:]
        print(str(r1))
        print(str(r2))
        print(str(r3))
        print("*********************")

    # Print this puzzle's solution chain (should be called when a solution is reached)
    def printSolution(self):
        puzzles = []
        while self:
            puzzles.append(self)
            self = self.prev
        puzzles.reverse()

        k = 0
        for p in puzzles:
            print("Step: ", k) if k != 0 else print("Initial State")
            p.printPuzzle()
            k += 1
        print("Solved!")

    # Determine if the puzzle is solvable (tile inversions must be even)
    def unsolvable(self):
        pass
