# 8-puzzle-solver
Python program to solve the 8-puzzle using several different searching algorithms, including A* Search, Greedy Search, Uniform-Cost Search
Breadth-First Search and Depth-First Search. See each algorithm's python file for detailed explanations on how the algorithm works. As 
well as the implementation.


### How To Use
After downloading the code, you can run the tests.py file to run tests for all algorithms. Each test will display
every move made on the puzzle until it has been solved, and the time elapsed. At the end of execution, 
the average running time of each algorithm will be displayed.

#### Adding Test Cases
To add a test case, convert your puzzle state into a 1-D array format, and use it to initialize a puzzle object in the tests list.
Puzzles are represented as 1-D lists, for example the puzzle [1, 2, 3, 4, 5, 6, 7, 8, 0] represents the solved state
[ 1, 2, 3
  4, 5, 6
  7, 8, 0 ]

Where 0 is the blank space.

### Picking Algorithms to Run
In the tests.py file, there is an enabled variable. To change which test to run, simply set the algorthm enabled to True/False. 

Here is a screenshot from the tests.py file with examples
![Test File](https://github.com/diciocciojoseph/8-puzzle-solver/sample_output/tests_file.png)

### Requirements
- Python 3
- A Text Editor of your choice
