def distances_acyclic(G, s):
    n = len(G)
    d = [float('inf')]*n
    d[s] = 0
    for u in dfs_postfixe(G, s):
        for v, w in G[u]:
            d[v] = min(d[v], d[u] + w)
    return d