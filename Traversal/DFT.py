def dfs(visited, graph, current_node):
    if current_node not in visited:
        visited.add(current_node)
        print(current_node, end=' ')
        for adj in graph[current_node]:
            dfs(visited, graph, adj)
            

graph = {
  '0' : ['1','2'],
  '1' : ['0', '2', '3'],
  '2' : ['0', '1', '4'],
  '3' : ['1', '4'],
  '4' : ['2', '3']
}

dfs(set(), graph, '0')        