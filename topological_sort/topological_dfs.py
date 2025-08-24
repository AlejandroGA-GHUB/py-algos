class Graph:
    
    def __init__(self):
        self.current_tasks_map = {}
        self.tasks_lists_seen = {}
    
    class GraphNode:
        def __init__(self, val: int):
            self.val = val
            self.dependencies = []
            # unvisited, visiting, visited
            self.visited_status = "Unvisited" 
        
    def process(self, tasks: list, dependencies_list: list[list]):

        current_tasks_as_tuple = tuple(tasks)

        if current_tasks_as_tuple not in self.tasks_lists_seen:
            print(f"First time processing...")
            self.create_graph_nodes(tasks, dependencies_list)
            arr = self.sort()
            self.tasks_lists_seen[current_tasks_as_tuple] = arr
            self.print_tasks(arr)
            self.current_tasks_map.clear()
            return
        
        print(f"Task list has been processed already, skipping the sorting step...")
        self.print_tasks(self.tasks_lists_seen[current_tasks_as_tuple])
    
    def create_graph_nodes(self, tasks: list, dependencies_list: list[list]):
        for task in tasks:
            current_node = self.GraphNode(task)
            self.current_tasks_map[task] = current_node
        
        # Set the dependencies of the node at pos 0 in the dependencies_list current list
        for list in dependencies_list:
            current_dependant = self.current_tasks_map[list[1]]
            self.current_tasks_map[list[0]].dependencies.append(current_dependant)

    def print_tasks(self, processed_tasks: list):
        for i in range(len(processed_tasks)):
            print(f"Task# {i} to do is: {processed_tasks[i]}")
        
    def sort(self) -> list:
        # No longer need local tasks_map, using self.current_tasks_map
        result_holder = []
        for graph_node in self.current_tasks_map.values():
            if graph_node.visited_status == "Unvisited":
                if not self.dfs(graph_node, result_holder):
                    return []  # Return empty list if cycle is detected
        
        result = []
        for val in reversed(result_holder):
            result.append(val)

        return result

    # [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]
    # 0 -> []
    # 1 -> []
    # 2 -> [3]
    # 3 -> [1]
    # 4 -> [0, 1]
    # 5 -> [0, 2]
    
    # Cycle case under
    # [[0, 1], [1, 2], [2, 0]]
    # 0 [1]
    # 1 [2]
    # 2 [0]
    # dfs traversal to find the order of the dependency list, must be reversed after
    def dfs(self, graph_node: GraphNode, result: list):
        if graph_node.visited_status == "Visited":
            return True
        if graph_node.visited_status == "Visiting":
            return False  # Found a cycle
        
        graph_node.visited_status = "Visiting"
        for current_node in graph_node.dependencies:
            if not self.dfs(current_node, result):
                return False  
        
        graph_node.visited_status = "Visited"
        result.append(graph_node.val)
        return True

    def test_processing(self):
        """Quick test method to verify DFS processing with 3 different scenarios"""
        print("=== DFS Topological Sort Testing ===\n")
        
        # Test Case 1: Linear dependencies (simple chain)
        print("Test 1: Linear Dependencies")
        tasks1 = [0, 1, 2, 3]
        dependencies1 = [[0, 1], [1, 2], [2, 3]]
        print(f"Tasks: {tasks1}")
        print(f"Dependencies: {dependencies1}")
        self.process(tasks1, dependencies1)
        print()
        
        # Test Case 2: Complex dependencies (multiple paths)
        print("Test 2: Complex Dependencies")
        tasks2 = [0, 1, 2, 3, 4, 5]
        dependencies2 = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]
        print(f"Tasks: {tasks2}")
        print(f"Dependencies: {dependencies2}")
        self.process(tasks2, dependencies2)
        print()
        
        # Test Case 3: Cycle detection
        print("Test 3: Cycle Detection")
        tasks3 = [0, 1, 2]
        dependencies3 = [[0, 1], [1, 2], [2, 0]]
        print(f"Tasks: {tasks3}")
        print(f"Dependencies: {dependencies3}")
        self.process(tasks3, dependencies3)
        print()
        
        print("=== Testing Complete ===")

# Quick test runner
if __name__ == "__main__":
    graph = Graph()
    graph.test_processing()
