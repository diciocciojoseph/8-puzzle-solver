import time
import puzzle
import bfs
import a_star
import greedy
import ucs
import heuristics

# Add Test Cases Here
tests = [
    puzzle.Puzzle([1, 2, 3, 4, 5, 6, 7, 0, 8]),
    puzzle.Puzzle([3, 6, 5, 7, 1, 8, 0, 2, 4]),
    puzzle.Puzzle([0, 3, 5, 1, 6, 8, 7, 2, 4]),
    puzzle.Puzzle([8, 7, 6, 5, 4, 3, 2, 1, 0]),
]

# Enable certain algorithms to run all tests
enabled = {
    "BFS":      True,
    "A*":       True,
    "GREEDY":   True,
    "UCS":      True,
}

# Helper function to handle test output


def run_test(search_alg, times, name):
    print("\n\n")
    print("Running Test: ", i+1, " with ", name)
    print("-------------------------------------------------------------------")
    start = time.time()
    search_alg(tests[i])
    diff = time.time()-start
    times.append(diff)
    print("Test: ", i+1, " Finished in: ", round(diff, 4))
    print("-------------------------------------------------------------------")
    print("\n\n")


# Run Tests With BFS
bfs_times = []
if enabled["BFS"]:
    for i in range(len(tests)):
        run_test(bfs.BFS, bfs_times, "BFS")

# Run Tests With A*
a_star_times = []
if enabled["A*"]:
    for i in range(len(tests)):
        run_test(a_star.A_STAR, a_star_times, "A*")

# Run Tests With Greedy Search
greedy_times = []
if enabled["GREEDY"]:
    for i in range(len(tests)):
        run_test(greedy.GREEDY, greedy_times, "GREEDY")

# Run Tests With UCS
ucs_times = []
if enabled["UCS"]:
    for i in range(len(tests)):
        run_test(ucs.UCS, ucs_times, "UCS")

# Display Average Runtimes of each Algorithm Across all test cases
if enabled["BFS"]:
    print("Average Running Time For BFS: ",
          round(sum(bfs_times)/len(bfs_times), 4))

if enabled["A*"]:
    print("Average Running Time For A*: ",
          round(sum(a_star_times)/len(a_star_times), 4))

if enabled["GREEDY"]:
    print("Average Running Time For GREEDY: ",
          round(sum(greedy_times)/len(greedy_times), 4))

if enabled["UCS"]:
    print("Average Running Time for UCS: ",
          round(sum(ucs_times)/len(ucs_times), 4))
