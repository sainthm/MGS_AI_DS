answer = 0
path = []

def DFS(v, n, ch, graph):
    global answer
    if v == n:
        answer += 1
        # print(path)
    else:
        for nv in graph[v]:
            if ch[nv] == 0:
                ch[nv] = 1
                path.append(nv)
                DFS(nv, n, ch, graph)
                ch[nv] = 0
                path.pop()

def solution(n, edge):
    global answer
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        
    ch = [0] * (n+1)
    ch[1] = 1
    path.append(1)
    DFS(1, n, ch, graph)
    return answer        

print(solution(5, [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 5], [3, 4], [4, 2], [4, 5]]))