import random

# Solution puzzle State (0 is blank space)
solution_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Puzzle Class
# Expects that the input puzzle contains distinct set of integers [0,8] 
# self.puzzle: Holds 1-D list representation of 3x3 puzzle board
# self.moves: Used to cache moves executed on the Puzzle
# Contains functions to solve the board

class Puzzle:
    def __init__(self, initial_puzzle, moves = []):
        self.puzzle = initial_puzzle
        self.moves = moves


    # Execute BFS traversal to find the solution in the least number of moves
    def getSolution(self):

        queue = [self]  # Initialize a python list representation of queue
        visited = {}    # Initialize a dict/map of visited puzzle states

        # Loop until every puzzle state has been visited
        while(queue):
            curr = queue.pop(0) # Get next puzzle in queue

            # Check if we have found the solution
            if curr.puzzle == solution_puzzle:
                curr.printSolPath()
                return

            # Mark the current puzzle as visited
            # Lists are not hashable, but can be hashed as stringified lists
            visited[str(curr.puzzle)] = True

            # Generate all "child" puzzles for every possible move
            nextPuzzles = curr.getNextPuzzles()

            # Append each non-visited child to the queue
            for p in nextPuzzles:
                if str(p.puzzle) not in visited:
                    queue.append(p)

        # If we have reached this point, the puzzle is unsolvable
        print("No Solution Found")
        print("")


    # Function to return all the possible next puzzles for a single move
    # Used to get the "children" of a partiuclar puzzle state
    def getNextPuzzles(self):

        # Get index of empty space, then calculate it's neighbors.
        spaceIdx = self.puzzle.index(0)

        # Get all adjacent items for a 3x3 board
        # If the blank spot is at i (mid), the following moves are possible:
        # x   i-3   x
        # i-1  i   i+1
        # x   i+3   x

        # Get all possible indexes of items that can be swapped

        # Get possible moves from "rows" above and below
        possibleMoves = []
        possibleMoves.append(spaceIdx - 3)
        possibleMoves.append(spaceIdx + 3)

        # Edge cases
        # if the blank space is at index 2 or 5 (right edge of board), 
        # we cannot move to i+1 (it swaps across board)
        # likewise we cannot move to i-1 at index 3 or 6 (left edge of board)
        if spaceIdx != 2 and spaceIdx != 5:
            possibleMoves.append(spaceIdx + 1)
        if spaceIdx != 3 and spaceIdx != 6:
            possibleMoves.append(spaceIdx-1)
        

        # Filter valid move by checking if the idx is within puzzle bounds
        validMoves = []
        for x in possibleMoves:
            if x >= 0 and x <= 8:
                validMoves.append(x)

        # Initialze and store a new puzzle for every valid move
        # Make a copy of the current puzzle and its moves
        # Execute one of the valid moves on it
        # Store the move made
        # Append it to newBoards list
        newPuzzles = []
        for valIdx in validMoves:
            p = Puzzle(self.puzzle[:], self.moves[:])  
            p.move(spaceIdx, valIdx)                   
            p.moves.append((spaceIdx, valIdx))         
            newPuzzles.append(p)                       

        return newPuzzles


    # Print out a readable display of the board
    # Uses list slicing to get a seperate list for each row
    def printPuzzle(self):
        print("*********************")
        r1 = self.puzzle[:3]
        r2 = self.puzzle[3:6]
        r3 = self.puzzle[6:]
        print(str(r1))
        print(str(r2))
        print(str(r3))
        print("*********************")


    # Swap elements i and j in the puzzle
    # By swapping with the blank space, we emulate making a puzzle piece move
    def move(self, i, j):
        if self.puzzle[i] != 0 and self.puzzle[j] != 0:
            print("Can only move if one element is a blank space!")
            return
        
        # Python style swap
        self.puzzle[i], self.puzzle[j] = self.puzzle[j], self.puzzle[i]
        

    # Function to print the solution path from a solved board state
    # Reverses and redos the moves made on the board, printing at each step
    def printSolPath(self):
        # Reverse Puzzle by applying all the moves in opposite order
        for x, y in reversed(self.moves):
            self.move(x, y)

        # Board should now be at initial state
        # Apply each move again in the original order, printing at each step
        print("Initial Puzzle (Step 0)")
        self.printPuzzle()
        i = 1
        for x, y in self.moves:
            self.move(x, y)
            print("Step " + str(i))
            self.printPuzzle()
            i += 1
        print("Puzzle Solved!")
        print("\n")






#-----------------------------------------------------------------------------
# Test Cases

print("Running All Test Cases... Please Wait\n")
# Case 1: Reversed Case (main test)
# Initial Puzzle = [8, 7, 6, 5, 4, 3, 2, 1, 0]

print("Test Case 1: Reversed")
print("------------------------------------------------------")
p1 = Puzzle([8, 7, 6, 5, 4, 3, 2, 1, 0])
p1.getSolution()

# Case 2: Trivial Case (requires only a single move)
# Initial Puzzle = [1, 0, 2, 3, 4, 5, 6, 7, 8]

print("Test Case 2: Trivial")
print("------------------------------------------------------")
p2 = Puzzle([1, 2, 3, 4, 5, 6, 7, 0, 8])
p2.getSolution()

# Case 3: Unsolvable Case (should print: No Solution Found)
# Initial Puzzle = [8, 1, 2, 0, 4, 3, 7, 6, 5]

# An input is insolvable if it has an odd number of inversions
# A pair of values is an inversion if they are in reverse order of the goal
# In this code, the inversion calculation is not done, 
# instead the queue in BFS will run empty and exit if no solution is found

print("Test Case 3: Unsolvable")
print("------------------------------------------------------")
p3 = Puzzle([8, 1, 2, 0, 4, 3, 7, 6, 5])
p3.getSolution()

# Case 4: Arbitrary Case
# Initial Puzzle = [3, 1, 2, 4, 7, 5, 6, 8, 0]

print("Test Case 4")
print("------------------------------------------------------")
p4 = Puzzle([3, 1, 2, 4, 7, 5, 6, 8, 0])
p4.getSolution()

# Case 5: Random Case
# Initial puzzle is [7, 1, 0, 6, 4, 5, 2, 3, 8] from seed 1234

# Set seed to 1234
random.seed(1234)
# Generates 9 distinct random numbers 0-8
randomLst = random.sample(range(9), 9)

print("Test Case 5: Randomized Input (Makes input from seed)")
print("------------------------------------------------------")
print("Generated List: " + str(randomLst))
p5 = Puzzle(randomLst)
p5.getSolution()

# End
#-----------------------------------------------------------------------------