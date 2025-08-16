class Topological_Sort:
    
    class GraphNode:
        def __init__(self, val: int):
            self.val = val
            self.dependencies = []
            # white = unvisited, gray = visiting, black = visited
            self.visited_status = "White"
        
    def sort(self, tasks: list, tasks_dependencies:list[list]):
        tasks_map = {}
        # Create the GraphNode for each individual task in tasks, and insert into the map
        self.create_graph_nodes(tasks, tasks_map)

        # Set the dependencies of the node at pos 0 in the tasks_dependencies current list
        for list in tasks_dependencies:
            current_dependant = tasks_map[list[1]]
            tasks_map[list[0]].dependencies.append(current_dependant)

        result_holder = []
        for graph_node in tasks_map.values():
            if graph_node.visited_status == "White":
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

    # [[0, 1], [1, 2], [2, 0]]
    # 0 [1]
    # 1 [2]
    # 2 [0]
    # dfs traversal to find the order of the dependency list, must be reversed after
    def dfs(self, graph_node: GraphNode, result: list):
        if graph_node.visited_status == "Black":
            return True
        if graph_node.visited_status == "Gray":
            return False  # Found a cycle
        
        graph_node.visited_status = "Gray"
        for current_node in graph_node.dependencies:
            if not self.dfs(current_node, result):
                return False  
        
        graph_node.visited_status = "Black"
        result.append(graph_node.val)
        return True

    def create_graph_nodes(self, tasks: list, tasks_map: map):
        for task in tasks:
            current_node = self.GraphNode(task)
            tasks_map[task] = current_node
