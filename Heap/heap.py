class BaseHeap:
    def __init__(self):
        self.data = [None]

    def pop(self):
        if len(self.data) == 2:
            return self.data.pop(1)
        answer = self.data[1]
        self.data[1] = self.data.pop(len(self.data)-1)
        self.sift_down()
        return answer

    def push(self, value):
        child_index = len(self.data)
        self.data.append(value)
        while child_index > 1:
            parent_index = child_index // 2
            if self.done_sifting_up(parent_index, value):
                break
            self.data[parent_index], self.data[child_index] = \
                self.data[child_index], self.data[parent_index]
            child_index = parent_index

    def done_sifting_up(self, parent_index, value):
        pass

    def index_for_swap(self, left_child):
        pass

    def done_sifting_down(self, parent_index, swap_index):
        pass

    def sift_down(self):
        parent_index = 1
        while True:
            left_child = parent_index * 2
            heap_size = len(self.data)
            if left_child >= heap_size:
                break
            right_child = left_child + 1
            if right_child >= heap_size:
                swap_index = left_child
            else:
                swap_index = self.index_for_swap(left_child)
            if self.done_sifting_down(parent_index, swap_index):
                break
            self.data[parent_index], self.data[swap_index] =\
                self.data[swap_index], self.data[parent_index]
            parent_index = swap_index

class MaxHeap(BaseHeap):
    def index_for_swap(self, left_child):
        right_child = left_child + 1
        if self.data[left_child] > self.data[right_child]:
            return left_child
        return right_child

    def done_sifting_down(self, parent_index, swap_index):
        return self.data[parent_index] >= self.data[swap_index]

    def done_sifting_up(self, parent_index, value):
        return self.data[parent_index] >= value

    def __repr__(self):
        return 'MaxHeap(' + str(self.data) + ')'


class MinHeap(BaseHeap):

    def done_sifting_down(self, parent_index, swap_index):
        return self.data[parent_index] <= self.data[swap_index]

    def done_sifting_up(self, parent_index, value):
        return self.data[parent_index] <= value

    def index_for_swap(self, left_child):
        right_child = left_child + 1
        if self.data[left_child] < self.data[right_child]:
            return left_child
        return right_child

    def __repr__(self):
        return 'MinHeap(' + str(self.data) + ')'
