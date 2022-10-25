def DFS(n):
    if n == 0:
        return
    else:
        # print(n)
        DFS(n-1)
        print(n, end= " ")

DFS(3)