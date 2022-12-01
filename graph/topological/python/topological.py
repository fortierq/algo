def dfs_postfixe(G, s):
    seen = [False]*len(G)
    L = []
    def aux(G, u):
        if not seen[u]:
            seen[u] = True
            for w in G[u]:
                aux(G, v)
            L.append(u)
    aux(G, s)
    return L[::-1] # inverse la liste