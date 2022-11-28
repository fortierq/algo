def bellman(g, r):
    n = len(g)
    d = [float("inf")]*n
    d[r] = 0
    for k in range(n - 2):
        for u in range(n):
            for v in range(len(g[u])):
                d[v] = min(d[v], d[u] + g[u][v])
    return d