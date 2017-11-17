import random
import heap

m = heap.RunningMedian()
for x in [13, 2, 7, 3, 19, 5, 11, 17]:
    m.add(x)
    print(str(m.sorted()) + " median = " + str(m.median()))