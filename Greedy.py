def path_h_cost(path):
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    return h_cost


def ucs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_h_cost) # Difference from A*
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
    "S": [("A", 1), ("B", 4)],
    "A": [("B", 2), ("C", 5), ("G", 12)],
    "B": [("C", 2)],
    "C": [("G", 3)],
}

H_table = {
    "S": 7,
    "A": 6,
    "B": 4,
    "C": 2,
    "G": 0,
}

solution = ucs(graph, "S", "G")
print("Solution is:", solution)
