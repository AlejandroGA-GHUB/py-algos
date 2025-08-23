# py-algos
Algorithm practice on python

## 📚 Algorithms Overview

This repository contains implementations of fundamental data structures and algorithms in Python, complete with comprehensive test suites.

## 🗂️ Data Structures & Algorithms

### 📊 Hash Table
**Location:** `hashtable/`

A custom hash table implementation with collision handling using chaining.

**Features:**
- Dynamic resizing when load factor exceeds threshold
- Collision resolution via separate chaining (linked lists)
- Standard operations: insert, search, delete
- Load factor monitoring for optimal performance

**Key Methods:**
- `put(key, value)` - Insert or update key-value pair
- `get(key)` - Retrieve value by key
- `remove(key)` - Delete key-value pair
- `resize()` - Dynamic array resizing

**Time Complexity:**
- Average: O(1) for all operations
- Worst case: O(n) when all keys hash to same bucket

---

### 🌳 Min Heap
**Location:** `minheap/`

A binary min-heap implementation where the smallest element is always at the root.

**Features:**
- Array-based binary tree representation
- Automatic heap property maintenance
- Parent-child relationship: `parent = (i-1)//2`, `children = 2*i+1, 2*i+2`

**Key Methods:**
- `insert(value)` - Add element while maintaining heap property
- `extract_min()` - Remove and return minimum element
- `peek()` - View minimum element without removal
- `heapify_up()` - Restore heap property upward
- `heapify_down()` - Restore heap property downward

**Time Complexity:**
- Insert: O(log n)
- Extract Min: O(log n)
- Peek: O(1)

**Use Cases:**
- Priority queues
- Heap sort algorithm
- Finding k smallest elements

---

### 🔄 Topological Sort
**Location:** `topological_sort/`

Two implementations of topological sorting for directed acyclic graphs (DAGs), useful for dependency resolution and task scheduling.

#### 🔍 BFS Implementation (Kahn's Algorithm)
**File:** `topological_bfs.py`

Uses breadth-first search with in-degree tracking.

**Algorithm:**
1. Calculate in-degree for each node
2. Add all nodes with in-degree 0 to queue
3. Process nodes from queue, reducing in-degrees of neighbors
4. Add nodes with in-degree 0 to queue
5. Repeat until queue is empty

**Features:**
- Cycle detection (returns empty list if cycle exists)
- Process caching for efficiency
- Lazy evaluation with `process()` method

#### 🌊 DFS Implementation
**File:** `topological_dfs.py`

Uses depth-first search with three-color marking system.

**Algorithm:**
1. Mark nodes as: Unvisited (white), Visiting (gray), Visited (black)
2. For each unvisited node, perform DFS
3. If gray node is encountered, cycle detected
4. Add nodes to result when fully processed
5. Reverse final result

**Color States:**
- **Unvisited**: Not yet explored
- **Visiting**: Currently being processed (in recursion stack)
- **Visited**: Completely processed

**Common Features (Both Implementations):**
- **Smart Caching**: Avoid re-sorting same task lists
- **Process Method**: High-level interface for task processing
- **Comprehensive Testing**: Multiple test scenarios included
- **Cycle Detection**: Handles invalid dependency graphs

**Time Complexity:** O(V + E) where V = vertices, E = edges

**Use Cases:**
- Build system dependency resolution
- Course prerequisite scheduling
- Project task ordering
- Package dependency management

## 🧪 Testing

Each algorithm includes comprehensive unit tests:

```bash
# Run specific algorithm tests
python -m pytest hashtable/test_hashtable.py
python -m pytest minheap/test_minheap.py
python -m pytest topological_sort/test_topological_sort.py

# Run all tests
python -m pytest
```

## 🚀 Usage Examples

### Hash Table
```python
from hashtable.hashtable import HashTable

ht = HashTable()
ht.put("key1", "value1")
ht.put("key2", "value2")
print(ht.get("key1"))  # Output: value1
```

### Min Heap
```python
from minheap.minheap import MinHeap

heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(15)
print(heap.extract_min())  # Output: 5
```

### Topological Sort
```python
from topological_sort.topological_bfs import Graph

graph = Graph()
tasks = [0, 1, 2, 3]
dependencies = [[0, 1], [1, 2], [2, 3]]  # 0→1→2→3
graph.process(tasks, dependencies)
# Output: Task processing in correct order
```

## 📈 Performance Characteristics

| Algorithm | Space | Insert/Add | Search/Find | Delete/Remove |
|-----------|-------|------------|-------------|---------------|
| Hash Table | O(n) | O(1) avg | O(1) avg | O(1) avg |
| Min Heap | O(n) | O(log n) | O(n) | O(log n) |
| Topological Sort | O(V+E) | - | - | - |

## 🎯 Learning Objectives

- **Data Structure Design**: Understanding internal workings of fundamental structures
- **Algorithm Analysis**: Time and space complexity evaluation
- **Problem Solving**: Real-world applications and use cases
- **Testing Practices**: Comprehensive test coverage and edge cases
- **Code Quality**: Clean, readable, and maintainable implementations
