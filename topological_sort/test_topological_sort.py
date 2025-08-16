import unittest
from topological_bfs import Topological_Sort as BFS_Sort
from topological_dfs import Topological_Sort as DFS_Sort

class TestTopologicalSort(unittest.TestCase):
    def setUp(self):
        self.bfs_sorter = BFS_Sort()
        self.dfs_sorter = DFS_Sort()
    
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
        
        bfs_result = self.bfs_sorter.sort(tasks, tasks_dependencies)
        dfs_result = self.dfs_sorter.sort(tasks, tasks_dependencies)
        
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
        
        self.assertEqual(self.bfs_sorter.sort(tasks, tasks_dependencies), [])
        self.assertEqual(self.dfs_sorter.sort(tasks, tasks_dependencies), [])

    def test_no_dependencies(self):
        """Test with tasks but no dependencies between them"""
        tasks = [0, 1, 2]
        tasks_dependencies = []
        
        bfs_result = self.bfs_sorter.sort(tasks, tasks_dependencies)
        dfs_result = self.dfs_sorter.sort(tasks, tasks_dependencies)
        
        # Results should contain all tasks in any order
        self.assertEqual(sorted(bfs_result), sorted(tasks))
        self.assertEqual(sorted(dfs_result), sorted(tasks))

    def test_linear_dependencies(self):
        """Test with linear dependencies (0->1->2->3)"""
        tasks = [0, 1, 2, 3]
        tasks_dependencies = [[0, 1], [1, 2], [2, 3]]
        
        bfs_result = self.bfs_sorter.sort(tasks, tasks_dependencies)
        dfs_result = self.dfs_sorter.sort(tasks, tasks_dependencies)
        
        # Both should respect the linear order
        self.assertEqual(bfs_result, [0, 1, 2, 3])
        self.assertEqual(dfs_result, [0, 1, 2, 3])

    def test_cycle_detection(self):
        """Test that cycles are detected and return empty list"""
        tasks = [0, 1, 2]
        tasks_dependencies = [[0, 1], [1, 2], [2, 0]]  # Creates a cycle
        
        bfs_result = self.bfs_sorter.sort(tasks, tasks_dependencies)
        dfs_result = self.dfs_sorter.sort(tasks, tasks_dependencies)
        
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
        
        bfs_result = self.bfs_sorter.sort(tasks, tasks_dependencies)
        dfs_result = self.dfs_sorter.sort(tasks, tasks_dependencies)
        
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
        
        self.assertEqual(self.bfs_sorter.sort(tasks, tasks_dependencies), [0])
        self.assertEqual(self.dfs_sorter.sort(tasks, tasks_dependencies), [0])

if __name__ == '__main__':
    unittest.main()
