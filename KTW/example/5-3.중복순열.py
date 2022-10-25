def DFS(L, n, k, p):
    if L == k:
        for x in p:
            print(x, end = " ")
        print()
    else:
        for i in range(1, n+1):
            p.append(i)
            DFS(L+1, n, k, p)
            p.pop()

print(DFS(0, 3, 2, []))