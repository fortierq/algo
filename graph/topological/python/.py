def dfs_postfixe(G, s):
    seen = [False]*len(G)
    L = []
    def aux(G, v):
        if not seen[v]:
            seen[v] = True
            for w in G[v]:
                aux(G, w)
            L.append(v)
    aux(G, s)
    return L[::-1] # inverse la liste