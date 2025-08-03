# my version
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # [9, 4, 7, 1, -2, 6, 5, 3]
    def buildHeap(self, array):
        # Write your code here.
        last_parent_idx = (len(array) - 2) // 2
        while last_parent_idx >= 0:
            self.siftDown(last_parent_idx, len(array) - 1, array)
            last_parent_idx -= 1

        return array

    def siftDown(self, current_idx, end_idx, heap):
        # Write your code here.
        child_one_idx = current_idx * 2 + 1

        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1

            smaller_child_idx = child_two_idx if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx] else child_one_idx

            if heap[smaller_child_idx] < heap[current_idx]:
                heap[current_idx], heap[smaller_child_idx] = heap[smaller_child_idx], heap[current_idx]
                current_idx = smaller_child_idx
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def siftUp(self, current_idx):
        # Write your code here.
        while current_idx > 0:
            parent_idx = (current_idx - 1) // 2

            if self.heap[current_idx] < self.heap[parent_idx]:
                self.heap[current_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[current_idx]
                current_idx = parent_idx
            else:
                return
        

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        removed_value = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return removed_value
        

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)