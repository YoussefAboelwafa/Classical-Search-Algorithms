def dfs(graph, start, goal):
    visited = []
    stack = [[start]]
    while stack:
        # pop from the back of the queue
        path = stack.pop()  # Difference from BFS
        node = path[-1]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            neighbours = graph.get(node, [])
            for neighbour in neighbours:
                new_path = path.copy()
                new_path.append(neighbour)
                stack.append(new_path)
    return "No path found"


graph = {
    "S": ["B", "D", "A"],
    "A": ["C"],
    "B": ["D"],
    "C": ["D", "G"],
    "D": ["G"],
}

solution = dfs(graph, "S", "G")
print("Solution is:", solution)
