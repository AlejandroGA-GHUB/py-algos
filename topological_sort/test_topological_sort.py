import unittest
from topological_bfs import Graph as BFS_Sort
from topological_dfs import Graph as DFS_Sort

class TestTopologicalSort(unittest.TestCase):
    
    def validate_dependencies(self, result: list, tasks_dependencies: list[list]) -> bool:
        """Helper method to verify all dependencies are satisfied in the result"""
        # Create position map for O(1) precedence checks
        position_map = {val: idx for idx, val in enumerate(result)}
        
        # Check each dependency pair
        for dependency in tasks_dependencies:
            task, dependent = dependency[0], dependency[1]
            if position_map[task] >= position_map[dependent]:
                return False
        return True

    def test_example_case(self):
        """Test the example case that was provided"""
        tasks = [0, 1, 2, 3, 4, 5]
        tasks_dependencies = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]
        
        # Create Graph instances with constructor parameters
        bfs_sorter = BFS_Sort(tasks, tasks_dependencies)
        dfs_sorter = DFS_Sort(tasks, tasks_dependencies)
        
        # Use process() method which handles everything internally
        print("=== BFS Processing ===")
        bfs_sorter.process()
        print("=== DFS Processing ===")
        dfs_sorter.process()
        
        # Get the cached results for validation
        current_deps_tuple = tuple(tuple(inner) for inner in tasks_dependencies)
        bfs_result = bfs_sorter.tasks_list_seen[current_deps_tuple]
        dfs_result = dfs_sorter.tasks_list_seen[current_deps_tuple]
        
        # Both should return valid results
        self.assertEqual(len(bfs_result), len(tasks))
        self.assertEqual(len(dfs_result), len(tasks))
        
        # Verify dependencies are satisfied in both results
        self.assertTrue(self.validate_dependencies(bfs_result, tasks_dependencies))
        self.assertTrue(self.validate_dependencies(dfs_result, tasks_dependencies))

    def test_empty_case(self):
        """Test with empty tasks and dependencies"""
        tasks = []
        tasks_dependencies = []
        
        # Create Graph instances with empty parameters
        bfs_sorter = BFS_Sort(tasks, tasks_dependencies)
        dfs_sorter = DFS_Sort(tasks, tasks_dependencies)
        
        # Use process() method which handles everything internally
        bfs_sorter.process()
        dfs_sorter.process()
        
        # Get the cached results for validation
        current_deps_tuple = tuple(tuple(inner) for inner in tasks_dependencies)
        bfs_result = bfs_sorter.tasks_list_seen[current_deps_tuple]
        dfs_result = dfs_sorter.tasks_list_seen[current_deps_tuple]
        
        self.assertEqual(bfs_result, [])
        self.assertEqual(dfs_result, [])

    def test_no_dependencies(self):
        """Test with tasks but no dependencies between them"""
        tasks = [0, 1, 2]
        tasks_dependencies = []
        
        bfs_sorter = BFS_Sort(tasks, tasks_dependencies)
        dfs_sorter = DFS_Sort(tasks, tasks_dependencies)
        
        # Use process() method which handles everything internally
        bfs_sorter.process()
        dfs_sorter.process()
        
        # Get the cached results for validation
        current_deps_tuple = tuple(tuple(inner) for inner in tasks_dependencies)
        bfs_result = bfs_sorter.tasks_list_seen[current_deps_tuple]
        dfs_result = dfs_sorter.tasks_list_seen[current_deps_tuple]
        
        # Results should contain all tasks in any order
        self.assertEqual(sorted(bfs_result), sorted(tasks))
        self.assertEqual(sorted(dfs_result), sorted(tasks))

    def test_linear_dependencies(self):
        """Test with linear dependencies (0->1->2->3)"""
        tasks = [0, 1, 2, 3]
        tasks_dependencies = [[0, 1], [1, 2], [2, 3]]
        
        bfs_sorter = BFS_Sort(tasks, tasks_dependencies)
        dfs_sorter = DFS_Sort(tasks, tasks_dependencies)
        
        # Use process() method which handles everything internally
        bfs_sorter.process()
        dfs_sorter.process()
        
        # Get the cached results for validation
        current_deps_tuple = tuple(tuple(inner) for inner in tasks_dependencies)
        bfs_result = bfs_sorter.tasks_list_seen[current_deps_tuple]
        dfs_result = dfs_sorter.tasks_list_seen[current_deps_tuple]
        
        # Both should respect the linear order
        self.assertEqual(bfs_result, [0, 1, 2, 3])
        self.assertEqual(dfs_result, [0, 1, 2, 3])

    def test_cycle_detection(self):
        """Test that cycles are detected and return empty list"""
        tasks = [0, 1, 2]
        tasks_dependencies = [[0, 1], [1, 2], [2, 0]]  # Creates a cycle
        
        bfs_sorter = BFS_Sort(tasks, tasks_dependencies)
        dfs_sorter = DFS_Sort(tasks, tasks_dependencies)
        
        # Use process() method which handles everything internally
        bfs_sorter.process()
        dfs_sorter.process()
        
        # Get the cached results for validation
        current_deps_tuple = tuple(tuple(inner) for inner in tasks_dependencies)
        bfs_result = bfs_sorter.tasks_list_seen[current_deps_tuple]
        dfs_result = dfs_sorter.tasks_list_seen[current_deps_tuple]
        
        # Both should detect cycle and return empty list
        self.assertEqual(bfs_result, [])
        self.assertEqual(dfs_result, [])

    def test_complex_dependencies(self):
        """Test with more complex dependencies"""
        tasks = [0, 1, 2, 3, 4]
        tasks_dependencies = [
            [0, 1], [0, 2],  # 0 must come before 1 and 2
            [1, 3], [2, 3],  # 1 and 2 must come before 3
            [3, 4]           # 3 must come before 4
        ]
        
        bfs_sorter = BFS_Sort(tasks, tasks_dependencies)
        dfs_sorter = DFS_Sort(tasks, tasks_dependencies)
        
        # Use process() method which handles everything internally
        bfs_sorter.process()
        dfs_sorter.process()
        
        # Get the cached results for validation
        current_deps_tuple = tuple(tuple(inner) for inner in tasks_dependencies)
        bfs_result = bfs_sorter.tasks_list_seen[current_deps_tuple]
        dfs_result = dfs_sorter.tasks_list_seen[current_deps_tuple]
        
        # Both should return valid results
        self.assertTrue(self.validate_dependencies(bfs_result, tasks_dependencies))
        self.assertTrue(self.validate_dependencies(dfs_result, tasks_dependencies))
        
        # Expected order: 0 -> (1,2) -> 3 -> 4
        self.assertEqual(bfs_result[0], 0)  # Should start with 0
        self.assertEqual(bfs_result[-1], 4) # Should end with 4
        self.assertEqual(dfs_result[0], 0)  # Should start with 0
        self.assertEqual(dfs_result[-1], 4) # Should end with 4

    def test_single_task(self):
        """Test with a single task"""
        tasks = [0]
        tasks_dependencies = []
        
        bfs_sorter = BFS_Sort(tasks, tasks_dependencies)
        dfs_sorter = DFS_Sort(tasks, tasks_dependencies)
        
        # Use process() method which handles everything internally
        bfs_sorter.process()
        dfs_sorter.process()
        
        # Get the cached results for validation
        current_deps_tuple = tuple(tuple(inner) for inner in tasks_dependencies)
        bfs_result = bfs_sorter.tasks_list_seen[current_deps_tuple]
        dfs_result = dfs_sorter.tasks_list_seen[current_deps_tuple]
        
        self.assertEqual(bfs_result, [0])
        self.assertEqual(dfs_result, [0])

    def test_process_method_integration(self):
        """Test the full process() method with caching functionality"""
        tasks = [0, 1, 2, 3]
        tasks_dependencies = [[0, 1], [1, 2], [2, 3]]
        
        # Test BFS process method
        bfs_sorter = BFS_Sort(tasks, tasks_dependencies)
        
        # First call should process normally
        print("=== Testing BFS process() method ===")
        bfs_sorter.process()
        
        # Second call should use cached result
        bfs_sorter.process()
        
        # Test DFS process method
        dfs_sorter = DFS_Sort(tasks, tasks_dependencies)
        
        print("\n=== Testing DFS process() method ===")
        dfs_sorter.process()
        
        # Second call should use cached result
        dfs_sorter.process()

    def test_callback_functionality(self):
        """Test the callback functionality in process() method"""
        tasks = [0, 1, 2]
        tasks_dependencies = [[0, 1], [1, 2]]
        
        # Track calls to verify callbacks work
        bfs_calls = []
        dfs_calls = []
        
        def bfs_callback(task_value, counter):
            bfs_calls.append((task_value, counter))
        
        def dfs_callback(task_value, counter):
            dfs_calls.append((task_value, counter))
        
        # Test BFS with custom callback
        bfs_sorter = BFS_Sort(tasks, tasks_dependencies)
        bfs_sorter.process(print_callback=bfs_callback)
        
        # Test DFS with custom callback
        dfs_sorter = DFS_Sort(tasks, tasks_dependencies)
        dfs_sorter.process(print_callback=dfs_callback)
        
        # Verify callbacks were called
        self.assertEqual(len(bfs_calls), 3)  # Should process 3 tasks
        self.assertEqual(len(dfs_calls), 3)  # Should process 3 tasks
        
        # Verify correct task values and counters
        expected_bfs = [(0, 1), (1, 2), (2, 3)]
        expected_dfs = [(0, 1), (1, 2), (2, 3)]
        
        self.assertEqual(bfs_calls, expected_bfs)
        self.assertEqual(dfs_calls, expected_dfs)

    def test_different_callbacks_per_call(self):
        """Test using different callbacks for different process() calls"""
        tasks = [0, 1, 2]
        tasks_dependencies = [[0, 1], [1, 2]]
        
        # Track different callback types
        default_calls = []
        custom_calls = []
        
        def custom_callback(task_value, counter):
            custom_calls.append(f"Custom: Task {task_value} at step {counter}")
        
        # Create a graph instance
        graph = BFS_Sort(tasks, tasks_dependencies)
        
        # First call with default printing (we can't easily capture print output in tests)
        # But we can verify it doesn't crash
        graph.process()
        
        # Get the result to verify it was cached
        current_deps_tuple = tuple(tuple(inner) for inner in tasks_dependencies)
        cached_result = graph.tasks_list_seen[current_deps_tuple]
        self.assertEqual(cached_result, [0, 1, 2])
        
        # Second call with custom callback (should use cached results)
        graph.process(print_callback=custom_callback)
        
        # Verify custom callback was called for cached results
        expected_custom = [
            "Custom: Task 0 at step 1",
            "Custom: Task 1 at step 2", 
            "Custom: Task 2 at step 3"
        ]
        self.assertEqual(custom_calls, expected_custom)

    def test_silent_callback(self):
        """Test using silent callback (no output)"""
        tasks = [0, 1, 2]
        tasks_dependencies = [[0, 1], [1, 2]]
        
        # Silent callback that does nothing
        def silent_callback(task_value, counter):
            pass  # No output
        
        # Should run without any output and not crash
        graph = BFS_Sort(tasks, tasks_dependencies)
        graph.process(print_callback=silent_callback)
        
        # Verify result is still correct
        current_deps_tuple = tuple(tuple(inner) for inner in tasks_dependencies)
        result = graph.tasks_list_seen[current_deps_tuple]
        self.assertEqual(result, [0, 1, 2])

if __name__ == '__main__':
    unittest.main()
