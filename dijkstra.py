def dijkstra(graph, start_node):
    vertex_count = len(graph)
    valid = [True] * vertex_count
    weight = [float('inf')] * vertex_count
    weight[start_node] = 0

    for _ in range(vertex_count):
        min_weight = float('inf')
        min_weight_id = -1
        for i in range(vertex_count):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                min_weight_id = i
        for i in range(vertex_count):
            if weight[min_weight_id] + graph[min_weight_id][i] < weight[i]:
                weight[i] = weight[min_weight_id] + graph[min_weight_id][i]
        valid[min_weight_id] = False
    return weight


def find_eccentricity(graph):
    eccentricity = []
    for i in range(len(graph)):
        eccentricity.append(max(dijkstra(graph, i)))
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
