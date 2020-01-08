import time
import puzzle
import bfs
import a_star

# Add Test Cases Here
tests = [
     puzzle.Puzzle([1, 2, 3, 4, 5, 6, 7, 0, 8]),
     puzzle.Puzzle([3, 6, 5, 7, 1, 8, 0, 2, 4]),
     puzzle.Puzzle([0, 3, 5, 1, 6, 8, 7, 2, 4]),
     puzzle.Puzzle([8, 7, 6, 5, 4, 3, 2, 1, 0]), # <--- Reversed / Worst Case (may take ~10s for bfs)
]

# Enable certain algorithms to run all tests
enabled = {
    "BFS":True,
    "A*":True,
}

# Run Tests With BFS
bfs_times = []
if enabled["BFS"]:
    for i in range(len(tests)):
        print("\n\n")
        print("Running Test: ", i+1, " with BFS")
        print("-------------------------------------------------------------------")
        bfs_start_time = time.time()
        bfs.BFS(tests[i])
        bfs_done = time.time()-bfs_start_time
        bfs_times.append(bfs_done)
        print("Test: ", i+1, " Finished in: ", round(bfs_done, 4))
        print("-------------------------------------------------------------------")
        print("\n\n")

# Run Tests With A*
a_star_times = []
if enabled["A*"]:
    for i in range(len(tests)):
        print("\n\n")
        print("Running Test: ", i+1, " with A*")
        print("-------------------------------------------------------------------")
        a_star_start_time = time.time()
        a_star.A_STAR(tests[i])
        a_star_done = time.time()-a_star_start_time
        a_star_times.append(a_star_done)
        print("Test: ", i+1, " Finished in: ", round(a_star_done, 4))
        print("-------------------------------------------------------------------")
        print("\n\n")

# Display Average Runtimes of each Algorithm Across all test cases
if enabled["BFS"]: print("Average Running Time For BFS: ", round(sum(bfs_times)/len(bfs_times), 4))
if enabled["A*"]: print("Average Running Time For A*: ", round(sum(a_star_times)/len(a_star_times), 4))