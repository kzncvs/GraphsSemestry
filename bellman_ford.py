def bf(graph, target):
    inf = float('inf')
    d = []
    for _ in range(len(graph)):
        d.append(inf)
    d[target] = 0

    for i in range(1, len(graph) - 1):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if d[v] > d[u] + graph[u][v]:
                    d[v] = d[u] + graph[u][v]
    return d


def find_eccentricity(graph):
    eccentricity = []
    for i in range(len(graph)):
        eccentricity.append(max(bf(graph, i)))
    return eccentricity


def find(graph):
    eccentricity = find_eccentricity(graph)
    centers = []
    min_ecc = float('inf')
    for i in range(len(graph)):
        if eccentricity[i] < min_ecc:
            centers.clear()
            centers.append(i)
            min_ecc = eccentricity[i]
        elif eccentricity[i] == min_ecc:
            centers.append(i)

    return centers
