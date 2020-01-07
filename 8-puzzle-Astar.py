
solution = [1, 2, 3, 4, 5, 6, 7, 8, 0]


class Puzzle:
    def __init__(self, state, depth, prev):
        self.state = state
        self.depth = depth
        self.prev = prev
        self.score = self.f()

    # Return manhattan distance from the board, used as heuristic
    def manhattan(self):
        for i in range(0, 9):
            score = 0
            if self.state[i] != i + 1 and self.state[i] != 0:
                correct_pos = 8 if self.state[i] == 0 else self.state[i] - 1
                s_row = int(i / 3)
                s_col = i % 3
                t_row = int(correct_pos / 3)
                t_col = correct_pos % 3
                score += abs(s_row - t_row) + abs(s_col - t_col)

        return score

    # Return puzzle score (depth + manhattan distance)
    def f(self):
        return self.depth + self.manhattan()

    # Return child instances of puzzle
    def expand(self):
        blank_idx = self.state.index(0)

        possibleMoves = []
        possibleMoves.append(blank_idx - 3)
        possibleMoves.append(blank_idx + 3)

        if blank_idx != 2 and blank_idx != 5:
            possibleMoves.append(blank_idx + 1)
        if blank_idx != 3 and blank_idx != 6:
            possibleMoves.append(blank_idx-1)

        validMoves = []
        for x in possibleMoves:
            if x >= 0 and x <= 8:
                validMoves.append(x)

        children = []
        for idx in validMoves:
            new_state = self.state[:]
            new_state[blank_idx], new_state[idx] = new_state[idx], new_state[blank_idx]
            children.append(Puzzle(new_state, self.depth + 1, self))

        return children


def printPuzzle(state):
    print("*********************")
    r1 = state[:3]
    r2 = state[3:6]
    r3 = state[6:]
    print(str(r1))
    print(str(r2))
    print(str(r3))
    print("*********************")

def getSolStates(puzzle):
    states = []
    while puzzle:
        states.append(puzzle.state)
        puzzle = puzzle.prev

    return list(reversed(states))

def printSol(states):
    i = 0
    for s in states:
        print("Step: ", i+1)
        printPuzzle(s)
        i += 1


def solve(initial_state):
    print("Solving...")
    cur = Puzzle(initial_state, 0, None)
    visited = {}
    unexplored = []

    while True:
        if cur.state == solution:
            states = getSolStates(cur)
            printSol(states)
            break
        else:
            visited[str(cur.state)] = True
            for child in cur.expand():
                if str(child.state) not in visited:
                    unexplored.append(child)

            unexplored.sort(key=lambda node: node.score, reverse=False)
            cur = unexplored.pop(0)

solve([8, 7, 6, 5, 4, 3, 2, 1, 0])