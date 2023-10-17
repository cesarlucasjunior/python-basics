# queues in python are double ended. That means that we can chance de start and finish queue.
# this allow us to perform i/o operations in constant time.

from collections import deque

# initializing a queue
queue = deque()

# appending at the end
queue.append(1)
queue.append(2)
print(queue)

# deleting from the beginnin
queue.popleft()
print(queue)

# appending from the beginning
queue.appendleft(1)
print(queue)

# deleting from the end
queue.pop()
print(queue)