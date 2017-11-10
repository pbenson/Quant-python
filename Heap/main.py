import random
import heap

m = heap.MaxHeap()
for _ in range(10):
    m.push(random.random())
while len(m.data) > 1:
    print(m.pop())
