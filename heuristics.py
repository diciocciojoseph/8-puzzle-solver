

def hamming(puzzle):
    h = 0
    for i in range(len(puzzle.state)):
        if puzzle.state[i] != puzzle.solution[i] and puzzle.state[i] != 0:
            h += 1
    return h


def manhattan(puzzle):
    return -1 
