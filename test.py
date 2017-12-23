from algorythms import bellman_ford as bf
from algorythms import floyd_warshall as fw
from algorythms import dijkstra as di
from time import time


def bellman(kek):
    start = time()
    bf.find(kek)
    return time() - start


def floyd(kek):
    start = time()
    fw.find(kek)
    return time() - start


def dij(kek):
    start = time()
    di.find(kek)
    return time() - start

