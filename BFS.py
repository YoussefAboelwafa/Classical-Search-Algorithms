def bfs(graph, start, goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            neighbours = graph.get(node, [])
            for neighbour in neighbours:
                new_path = path.copy()
                new_path.append(neighbour)
                queue.append(new_path)
    return "No path found"


graph = {
    "S": ["B", "D", "A"],
    "A": ["C"],
    "B": ["D"],
    "C": ["G", "D"],
    "D": ["G"],
}

solution = bfs(graph, "S", "G")
print("Solution is:", solution)
