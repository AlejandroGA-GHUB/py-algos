from collections import deque as q 

# 1) Implement topological sort in python
# 2) implement using both: bfs and dfs
# 3) Use copilot for code improvement and test cases for both (bfs,dfs)
# 4) check-in the code to github when done

# Im a user with a tasklist and dependencies, create the graph and process it. Call a method called process(). This will call sort()
# and then the process of the task ie. print each task 
# [0, 1, 2]
# sort()
# 0, 1, 2

# add some logic to not always need to sort if its already been done

class Graph: 

    current_tasks_map = {}
    tasks_lists_seen = {}
    
    class GraphNode: 
        def __init__(self, val: int):
            self.val = val
            self.indegree = 0
            self.dependencies = []

    # [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]
    # 0 -> []
    # 1 -> []
    # 2 -> [3]
    # 3 -> [1]
    # 4 -> [0, 1]
    # 5 -> [0, 2]
    # [0, 1, 2, 3, 4, 5]
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

    def print_tasks(self, processed_tasks: list):
        for i in range(len(processed_tasks)):
            print(f"Task# {i} to do is: {processed_tasks[i]}")
    
    def create_graph_nodes(self, tasks: list, dependencies_list: list[list]):
        for task in tasks:
            current_node = self.GraphNode(task)
            self.current_tasks_map[task] = current_node # {1: graphnode of 1}
        
        # Set the indegree of the dependant, position [, x] to + 1 and add the same position node to the dependencies of pos 0
        for list in dependencies_list:
            current_dependant = self.current_tasks_map[list[1]]
            current_dependant.indegree += 1

            current_prereq = self.current_tasks_map[list[0]]
            current_prereq.dependencies.append(current_dependant)

    def sort(self) -> list:

        completed_tasks = q()
        # Find indegree 0's to start the queue with
        for graph_node in self.current_tasks_map.values():
            if graph_node.indegree == 0:
                completed_tasks.append(graph_node)

        result = []
        # Add the completed tasks to results and traverse its dependencies
        while len(completed_tasks) != 0:
            completed_task = completed_tasks.popleft()
            result.append(completed_task.val)

            for graph_node in completed_task.dependencies:
                graph_node.indegree -= 1
                if graph_node.indegree == 0:
                    completed_tasks.append(graph_node)
        
        # Check length as an equal length to the original array implies that it had a valid dependency order
        return result if len(result) == len(self.current_tasks_map) else []

    def test_processing(self):
        """Quick test method to verify BFS processing with 3 different scenarios"""
        print("=== BFS Topological Sort Testing ===\n")
        
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

