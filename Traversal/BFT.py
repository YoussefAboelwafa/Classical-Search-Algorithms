from queue import SimpleQueue

def bfs(graph, initial_vertex):
  visited_vertices = []
  bfs_queue = SimpleQueue()
  visited_vertices.append(initial_vertex)
  bfs_queue.put(initial_vertex)

  while not bfs_queue.empty():
    current_vertex = bfs_queue.get()
    print(current_vertex, end=" ")
    for adjacent_vertex in graph[current_vertex]:
      if adjacent_vertex not in visited_vertices:
        visited_vertices.append(adjacent_vertex)
        bfs_queue.put(adjacent_vertex)


graph = {
  '4' : ['6','7'],
  '6' : ['4', '7', '8'],
  '7' : ['4', '6', '9'],
  '8' : ['6', '9'],
  '9' : ['7', '8']
}

bfs(graph, '4')