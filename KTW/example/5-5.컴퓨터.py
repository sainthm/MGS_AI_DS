cnt = 0
def DFS(v, n, ch, graph):
    global cnt
    cnt += 1
    for nv in graph[v]:
        if ch[nv] == 0:
            ch[nv] = 1
            DFS(nv, n, ch, graph)


def solution(n, edge):
    global cnt
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    ch = [0] * (n+1)
    ch[1] = 1
    DFS(1, n, ch, graph)
    return n - cnt

print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))