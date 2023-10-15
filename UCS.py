def path_cost(path):
    cost = 0
    for node, weight in path:
        cost += weight
    return cost


def ucs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)  # Difference from Greedy
        path = queue.pop(0)
        node = path[-1][0]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            neighbours = graph.get(node, [])
            for neighbour, cost in neighbours:
                new_path = path.copy()
                new_path.append((neighbour, cost))
                queue.append(new_path)
    return "No path found"


graph = {
    "S": [("A", 2), ("B", 3), ("D", 5)],
    "A": [("C", 4)],
    "B": [("D", 4)],
    "C": [("D", 1), ("G", 2)],
    "D": [("G", 5)],
}

solution = ucs(graph, "S", "G")
print("Solution is:", solution)
print("Path cost is:", path_cost(solution))
