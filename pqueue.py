import heapq

# Priority Queue using python's heapq module (min-heap)
# The item with the highest priority will be kept on top of the heap in accordance with the given priority function
# self.key = function to decide priority (for example, hamming distance)
# self.data = list which will store the data (will maintain heap invariant with pops/pushes)
class PriorityQueue:
    def __init__(self, key):
        self.key = key
        self.data = []

    def push(self, item):
        # Python heapq allows a tuple to be passed, with the first element being the priorty function,
        # and the second is the item to be pushed
        # In our case, we will be pushing Puzzle objects which require some sort of scoring function
        heapq.heappush(self.data, (self.key(item), item))

    def pop(self):
        # Pops the element with highest priority
        return heapq.heappop(self.data)[1]