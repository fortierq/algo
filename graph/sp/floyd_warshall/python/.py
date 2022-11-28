import copy

def floyd_warshall(g):
    n = len(g)
    d = copy.deepcopy(g) # pour éviter de modifier g
    for k in range(n):
        for u in range(n):
            for v in range(n):
                d[u][v] = min(d[u][v], d[u][k] + d[k][v])
    return d