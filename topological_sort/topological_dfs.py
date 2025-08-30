class Graph:
    
    def __init__(self, tasks: list, dependencies_list: list[list]):
        self.current_tasks_map = {}
        self.tasks_list_seen = {}
        self.tasks = tasks
        self.dependencies_list = dependencies_list
    
    class GraphNode:
        def __init__(self, val: int):
            self.val = val
            self.dependencies = []
            # unvisited, visiting, visited
            self.visited_status = "Unvisited" 
        
    def process(self, print_callback=None):

        # Use provided callback or default print behavior
        self.print_callback = print_callback or self.default_print_task

        current_dependencies_list = tuple(tuple(inner) for inner in self.dependencies_list)

        if current_dependencies_list not in self.tasks_list_seen:
            print(f"First time processing...")
            self.create_graph_nodes()
            arr = self.sort()
            self.tasks_list_seen[current_dependencies_list] = arr
            return
        
        print(f"Task list has been processed already, skipping the sorting step...")
        arr = self.tasks_list_seen[current_dependencies_list]
        for i, task_val in enumerate(arr):
            self.print_callback(task_val, i+1)

    def default_print_task(self, task_value, counter: int):
        """Default printing behavior"""
        print(f"Task# {counter} to do is: {task_value}")
    
    def create_graph_nodes(self):
        for task in self.tasks:
            current_node = self.GraphNode(task)
            self.current_tasks_map[task] = current_node
        
        # Set the dependencies of the node at pos 0 in the dependencies_list current list
        for list in self.dependencies_list:
            current_dependant = self.current_tasks_map[list[1]]
            self.current_tasks_map[list[0]].dependencies.append(current_dependant)
        
    def sort(self) -> list:
        # No longer need local tasks_map, using self.current_tasks_map
        result_holder = []
        for graph_node in self.current_tasks_map.values():
            if graph_node.visited_status == "Unvisited":
                if not self.dfs(graph_node, result_holder):
                    return []  # Return empty list if cycle is detected
        
        result = []
        task_counter = 1
        for val in reversed(result_holder):
            result.append(val)
            self.print_callback(val, task_counter)
            task_counter += 1

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

def test_processing():
    """Quick test method to verify DFS processing with callback functionality"""
    print("=== DFS Topological Sort Testing ===\n")
    
    # Custom callback functions for demonstration
    def fancy_print(task_value, counter):
        print(f"🚀 DFS Processing Task {task_value} (Step #{counter})")
    
    def minimal_print(task_value, counter):
        print(f"{counter}: {task_value}")
    
    def verbose_print(task_value, counter):
        print(f">>> DFS: Task {task_value} completed at position {counter} <<<")
    
    # Test Case 1: Linear dependencies with default printing
    print("Test 1: Linear Dependencies (Default Printing)")
    tasks1 = [0, 1, 2, 3]
    dependencies1 = [[0, 1], [1, 2], [2, 3]]
    print(f"Tasks: {tasks1}")
    print(f"Dependencies: {dependencies1}")
    graph1 = Graph(tasks1, dependencies1)
    graph1.process()  # No callback = default printing
    print()
    
    # Test Case 2: Complex dependencies with fancy printing
    print("Test 2: Complex Dependencies (Fancy Printing)")
    tasks2 = [0, 1, 2, 3, 4, 5]
    dependencies2 = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]
    print(f"Tasks: {tasks2}")
    print(f"Dependencies: {dependencies2}")
    graph2 = Graph(tasks2, dependencies2)
    graph2.process(print_callback=fancy_print)  # Custom callback
    print()
    
    # Test Case 3: Cycle detection with minimal printing
    print("Test 3: Cycle Detection (Minimal Printing)")
    tasks3 = [0, 1, 2]
    dependencies3 = [[0, 1], [1, 2], [2, 0]]
    print(f"Tasks: {tasks3}")
    print(f"Dependencies: {dependencies3}")
    graph3 = Graph(tasks3, dependencies3)
    graph3.process(print_callback=minimal_print)  # Another custom callback
    print()
    
    # Test Case 4: Testing cached processing with different callback
    print("Test 4: Cached Processing (Different Callback)")
    print("Reusing graph2 with verbose printing...")
    graph2.process(print_callback=verbose_print)  # Different callback for cached result
    print()
    
    print("=== Testing Complete ===")

# Quick test runner
if __name__ == "__main__":
    test_processing()
