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
