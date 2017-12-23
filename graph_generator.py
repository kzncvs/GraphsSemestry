import random


def generate(vertex_count, edge_count):
    inf = float('inf')
    graph = []
    for _ in range(vertex_count):
        graph.append([inf] * vertex_count)
    for i in range(len(graph)):
        graph[i][i] = 0

    added = 0
    while True:
        x = random.randint(0, vertex_count - 1)
        y = random.randint(0, vertex_count - 1)
        if graph[x][y] == inf:
            new = random.randint(1, 20)
            graph[x][y] = new
            graph[y][x] = new
            added += 1
        if added == edge_count:
            break
    return graph
