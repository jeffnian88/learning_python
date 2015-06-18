from collections import deque
list_ = [1,2,3]
queue = deque(list_)

# insert
queue.append(4)
print queue

# pop
queue.popleft()
print queue
