from collections import deque as q

# 1) Implement topological sort in python
# 2) add it to algos github
# 3) implement using both: bfs and dfs
# 4) Use copilot for code improvement and test cases for both (bfs,dfs)
# 5) check-in the code to github when done

class Topological_Sort:
    
    class GraphNode:
        def __init__(self, val: int):
            self.val = val
            self.indegree = 0
            self.dependencies = []

    def sort(self, tasks: list, tasks_dependencies:list[list]):
        tasks_map = {}
        # Create the GraphNode for each individual task in tasks, and insert into the map
        self.create_graph_nodes(tasks, tasks_map)

        # Set the indegree of the dependant, position [, x] to + 1 and add the same position node to the dependencies of pos 0
        for list in tasks_dependencies:
            current_dependant = tasks_map[list[1]]
            current_dependant.indegree += 1
            tasks_map[list[0]].dependencies.append(current_dependant)

        completed_tasks = q()
        # Find indegree 0's to start the queue with
        for graph_node in tasks_map.values():
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
        
        return result if len(result) == len(tasks) else []

    def create_graph_nodes(self, tasks: list, tasks_map: map):
        for task in tasks:
            current_node = self.GraphNode(task)
            tasks_map[task] = current_node

