import pytest
from minheap import MinHeap

@pytest.fixture
def sample_heap():
    return MinHeap([9, 4, 7, 1, -2, 6, 5, 3])

def test_build_heap():
    arr = [9, 4, 7, 1, -2, 6, 5, 3]
    heap = MinHeap(arr)
    for i in range((len(heap.heap) - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(heap.heap):
            assert heap.heap[i] <= heap.heap[left]
        if right < len(heap.heap):
            assert heap.heap[i] <= heap.heap[right]

def test_peek(sample_heap):
    assert sample_heap.peek() == -2

def test_insert(sample_heap):
    sample_heap.insert(-5)
    assert sample_heap.peek() == -5
    sample_heap.insert(10)
    assert sample_heap.peek() == -5
    sample_heap.insert(-10)
    assert sample_heap.peek() == -10

def test_remove(sample_heap):
    min_val = sample_heap.remove()
    assert min_val == -2
    assert sample_heap.peek() == 1
    min_val2 = sample_heap.remove()
    assert min_val2 == 1
    assert sample_heap.peek() == 3

def test_siftUp_and_siftDown():
    heap = MinHeap([5, 7, 9, 1, 3])
    heap.insert(0)
    assert heap.peek() == 0
    heap.remove()
    assert heap.peek() == 1

def test_heap_property_after_operations():
    heap = MinHeap([])
    for val in [3, 1, 6, 5, 2, 4]:
        heap.insert(val)
    for i in range((len(heap.heap) - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(heap.heap):
            assert heap.heap[i] <= heap.heap[left]
        if right < len(heap.heap):
            assert heap.heap[i] <= heap.heap[right]