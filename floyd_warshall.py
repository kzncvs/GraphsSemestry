def floyd_warshall(gr):
    graph = gr.copy()
    for k in range(0, len(graph)):
        for i in range(0, len(graph)):
            for j in range(0, len(graph)):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph


def find_eccentricity(graph):
    eccentricity = []
    gr = floyd_warshall(graph)
    for i in range(len(graph)):
        eccentricity.append(max((gr[i])))
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
