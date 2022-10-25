edges = [[0, 1], [0, 2], [1, 2], [2, 3], [2, 5], [3, 4], [3, 5]]

graph = [[]] for _ in rane(6)]

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

[
    [1, 2],
    [0, 2],
    [0, 1, 3, 5],
    [2, 4, 5],
    [3],
    [2, 3]
]