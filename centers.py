import dijkstra as di


def find_eccentricity(graph):
    eccentricity = []
    for i in range(len(graph)):
        eccentricity.append(max(di.dijkstra(graph, i)))
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
