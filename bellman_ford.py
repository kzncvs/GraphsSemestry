def bellman_ford(graph, target):
    inf = float('inf')
    distance = []
    for _ in range(len(graph)):
        distance.append(inf)
    distance[target] = 0

    for i in range(1, len(graph) - 1):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]
    return distance


def find_eccentricity(graph):
    eccentricity = []
    for i in range(len(graph)):
        eccentricity.append(max(bellman_ford(graph, i)))
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
