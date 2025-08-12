from typing import List
import heapq

#heapq module
# 1) create heap from array and from empty list/array
# 2) test gainst python heapq api. Use heapify()
# 3) Use Copilot to test against heapq
# # my version
# build minheap from an empty array inserting with insert()
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = []
        self.buildHeap(array)

    # example passed in [9, 4, 7, -2, 6, 5]
    def buildHeap(self, array):
        # Write your code here.
        if array is None or len(array) == 0:
            return

        for i in range(len(array)):
            self.insert(array[i])

    # Takes in a heap as opposed to explicitly using self.heap as it's also used for testing
    def print_heap_as_array(self, heap):
        print(f"Current heap as an array: {heap}")

    def siftDown(self, current_idx, end_idx, heap):
        # Write your code here.
        child_one_idx = self.find_left_child_idx(current_idx)

        while child_one_idx <= end_idx:
            child_two_idx = self.find_right_child_idx(current_idx)

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
            parent_idx = self.find_parent_idx(current_idx)

            if self.heap[current_idx] < self.heap[parent_idx]:
                self.heap[current_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[current_idx]
                current_idx = parent_idx
            else:
                return
    
    def find_left_child_idx(self, parent_idx):
        return parent_idx * 2 + 1
    
    def find_right_child_idx(self, parent_idx):
        return parent_idx * 2 + 2 if parent_idx * 2 + 2 <= len(self.heap) - 1 else -1
    
    def find_parent_idx(self, child_idx):
        return (child_idx - 1) // 2

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

#
#
#
#
#
#
#
#
#
#

# # optimized version (copilot)
# class MinHeap:
#     def __init__(self, initial_array: List[int]):
#         """Initialize MinHeap with an optional initial array"""
#         self.heap = self.buildHeap(initial_array.copy())  # Avoid modifying input array

#     def buildHeap(self, array: List[int]) -> List[int]:
#         """Build a min heap from an unordered array in O(n) time"""
#         first_parent = (len(array) - 2) // 2
#         for i in range(first_parent, -1, -1):
#             self._siftDown(i, array)
#         return array

#     def _siftDown(self, current: int, heap: List[int]) -> None:
#         """Move element down the heap until heap property is restored"""
#         heap_size = len(heap)
#         while True:
#             smallest = current
#             left = 2 * current + 1
#             right = 2 * current + 2

#             if left < heap_size and heap[left] < heap[smallest]:
#                 smallest = left
#             if right < heap_size and heap[right] < heap[smallest]:
#                 smallest = right

#             if smallest == current:
#                 break

#             heap[current], heap[smallest] = heap[smallest], heap[current]
#             current = smallest

#     def _siftUp(self, index: int) -> None:
#         """Move element up the heap until heap property is restored"""
#         while index > 0:
#             parent = (index - 1) // 2
#             if self.heap[index] >= self.heap[parent]:
#                 break
#             self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
#             index = parent

#     def peek(self) -> int:
#         """Return the minimum element without removing it"""
#         if not self.heap:
#             raise IndexError("Heap is empty")
#         return self.heap[0]

#     def remove(self) -> int:
#         """Remove and return the minimum element"""
#         if not self.heap:
#             raise IndexError("Heap is empty")

#         min_val = self.heap[0]
#         last_val = self.heap.pop()

#         if self.heap:  # If heap not empty after pop
#             self.heap[0] = last_val
#             self._siftDown(0, self.heap)

#         return min_val

#     def insert(self, value: int) -> None:
#         """Insert a new value into the heap"""
#         self.heap.append(value)
#         self._siftUp(len(self.heap) - 1)