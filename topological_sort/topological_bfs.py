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

    def __init__(self, tasks: list, dependencies_list: list[list]):
        self.current_tasks_map = {}
        self.tasks_list_seen = {}
        self.tasks = tasks
        self.dependencies_list = dependencies_list
    
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

    def modify():
        pass
    
    # look into callback for process and fix the constructor logic
    # fix sort logic for printing
    # fix completed_tasks naming
    # process and subsequent functions call with no args except the function to call if implemented
    def process(self):

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
            print(f"Task# {i+1} to do is: {task_val}")

    def print_task(self, processed_task, counter: int):
        print(f"Task# {counter} to do is: {processed_task.val}")
    
    def create_graph_nodes(self):
        for task in self.tasks:
            current_node = self.GraphNode(task)
            self.current_tasks_map[task] = current_node # {1: graphnode of 1}
        
        # Set the indegree of the dependant, position [, x] to + 1 and add the same position node to the dependencies of pos 0
        for list in self.dependencies_list:
            current_dependant = self.current_tasks_map[list[1]]
            current_dependant.indegree += 1

            current_prereq = self.current_tasks_map[list[0]]
            current_prereq.dependencies.append(current_dependant)

    def sort(self) -> list:

        tasks_to_process = q()
        # Find indegree 0's to start the queue with
        for graph_node in self.current_tasks_map.values():
            if graph_node.indegree == 0:
                tasks_to_process.append(graph_node)

        result = []
        task_counter = 1
        # Add the completed tasks to results and traverse its dependencies
        while len(tasks_to_process) != 0:
            current_task = tasks_to_process.popleft()
            result.append(current_task.val)
            self.print_task(current_task, task_counter)
            task_counter += 1

            for graph_node in current_task.dependencies:
                graph_node.indegree -= 1
                if graph_node.indegree == 0:
                    tasks_to_process.append(graph_node)
        
        # Check length as an equal length to the original array implies that it had a valid dependency order
        return result if len(result) == len(self.current_tasks_map) else []


def test_processing():
    """Quick test method to verify BFS processing with 3 different scenarios"""
    print("=== BFS Topological Sort Testing ===\n")
    
    # Test Case 1: Linear dependencies (simple chain)
    print("Test 1: Linear Dependencies")
    tasks1 = [0, 1, 2, 3]
    dependencies1 = [[0, 1], [1, 2], [2, 3]]
    print(f"Tasks: {tasks1}")
    print(f"Dependencies: {dependencies1}")
    graph1 = Graph(tasks1, dependencies1)
    graph1.process()
    print()
    
    # Test Case 2: Complex dependencies (multiple paths)
    print("Test 2: Complex Dependencies")
    tasks2 = [0, 1, 2, 3, 4, 5]
    dependencies2 = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]
    print(f"Tasks: {tasks2}")
    print(f"Dependencies: {dependencies2}")
    graph2 = Graph(tasks2, dependencies2)
    graph2.process()
    print()
    
    # Test Case 3: Cycle detection
    print("Test 3: Cycle Detection")
    tasks3 = [0, 1, 2]
    dependencies3 = [[0, 1], [1, 2], [2, 0]]
    print(f"Tasks: {tasks3}")
    print(f"Dependencies: {dependencies3}")
    graph3 = Graph(tasks3, dependencies3)
    graph3.process()
    print()
    
    print("=== Testing Complete ===")


# Quick test runner
if __name__ == "__main__":
    test_processing()

