# This module is dedicated to the implementation of the heuristics used to score an 8-puzzle state
# Hamming Priority: Counts the number of misplaced tiles on the board
# Manhattan Priority: Calculates the distance of each tile from it's solved position


def hamming(puzzle):
    h = 0
    for i in range(len(puzzle.state)):
        if puzzle.state[i] != puzzle.solution[i] and puzzle.state[i] != 0:
            h += 1
    return h


def manhattan(puzzle):
    score = 0
    for i in range(1, 9):
        for stateVal, goalVal in ((puzzle.state.index(i), puzzle.solution.index(i))):
            score += (abs(stateVal % 3 - goalVal % 3) +
                      abs(stateVal // 3 - goalVal // 3))
    return score
