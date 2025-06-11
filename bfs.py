def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue += graph[node]
    
    return visited

# Example graph
graph = {
    'A': ['B', 'F'],
    'B': ['D', 'E'],
    'C': ['F','A'],
    'D': ['C'],
    'E': ['F'],
    'F': []
}

print("BFS:", bfs(graph, 'A'))
