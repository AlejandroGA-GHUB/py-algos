import pytest
from minheap import MinHeap
import heapq

@pytest.fixture
def empty_heap():
    return MinHeap([])

@pytest.fixture
def built_heap():
    return MinHeap([9, 4, 7, 1, -2, 6, 5, 3])

def test_empty_heap_initialization(empty_heap):
    assert len(empty_heap.heap) == 0

def test_manual_insertion(empty_heap):
    values = [9, 4, 7, 1, -2, 6, 5, 3]
    for value in values:
        empty_heap.insert(value)
    
    # Test heap property after manual insertions
    heap_array = empty_heap.heap
    for i in range(len(heap_array)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(heap_array):
            assert heap_array[i] <= heap_array[left]
        if right < len(heap_array):
            assert heap_array[i] <= heap_array[right]

def test_build_heap_initialization(built_heap):
    # Test heap property after buildHeap
    heap_array = built_heap.heap
    for i in range(len(heap_array)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(heap_array):
            assert heap_array[i] <= heap_array[left]
        if right < len(heap_array):
            assert heap_array[i] <= heap_array[right]

def test_peek_empty_and_filled(empty_heap, built_heap):
    assert built_heap.peek() == -2
    with pytest.raises(IndexError):
        empty_heap.peek()

def test_insert_to_empty(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.peek() == 5
    empty_heap.insert(3)
    assert empty_heap.peek() == 3
    empty_heap.insert(7)
    assert empty_heap.peek() == 3

def test_remove_until_empty(built_heap):
    values = []
    initial_size = len(built_heap.heap)
    
    # Remove all elements and verify they come out in ascending order
    for _ in range(initial_size):
        values.append(built_heap.remove())
    
    assert values == sorted(values)
    assert len(built_heap.heap) == 0

def test_mixed_operations(empty_heap):
    # Test sequence of insertions and removals
    empty_heap.insert(5)
    empty_heap.insert(3)
    assert empty_heap.remove() == 3
    empty_heap.insert(7)
    empty_heap.insert(1)
    assert empty_heap.remove() == 1
    assert empty_heap.peek() == 5

def test_remove_from_empty(empty_heap):
    with pytest.raises(IndexError):
        empty_heap.remove()

def verify_heap_property(heap_array):
    """Helper function to verify min heap properties"""
    for i in range(len(heap_array)):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check left child if it exists
        if left < len(heap_array):
            if heap_array[i] > heap_array[left]:
                return False
        
        # Check right child if it exists
        if right < len(heap_array):
            if heap_array[i] > heap_array[right]:
                return False
    return True

def test_heap_matches_heapified_version():
    # Test different arrays
    test_arrays = [
        [9, 4, 7, 1, -2, 6, 5, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [-1, -5, 0, 10, 3]
    ]
    
    for arr in test_arrays:
        # Build our heap
        heap = MinHeap(arr)
        # Create heapified version of our final heap
        heapified = heap.heap.copy()
        heapq.heapify(heapified)

        heap.print_heap_as_array(heap.heap)
        heap.print_heap_as_array(heapified)
        
        # Compare my heap implementation with heapq's in heap building via array 
        assert heap.heap == heapified, f"Mismatch"

def test_manual_heap_matches_heapified_version():
    # Test different arrays
    test_arrays = [
        [9, 4, 7, 1, -2, 6, 5, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [-1, -5, 0, 10, 3]
    ]
    
    for arr in test_arrays:
        # Build heap manually through insertions
        heap = MinHeap([])  # Start with empty heap
        for value in arr:
            heap.insert(value)
            
        # Create heapified version of our final heap
        heapified = heap.heap.copy()
        heapq.heapify(heapified)

        heap.print_heap_as_array(heap.heap)
        heap.print_heap_as_array(heapified)
        
        # Compare my heap implementation with heapq's in manual insertion
        assert heap.heap == heapified, f"Mismatch"