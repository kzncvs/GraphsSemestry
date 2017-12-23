from algorythms import bellman_ford as bf
from algorythms import floyd_warshall as fw
from algorythms import dijkstra as di

i = float('inf')

g1 = [[0.0, 7.0, 9.0, i, i, 14],
      [7.0, 0.0, 10.0, 15.0, i, i],
      [9.0, 10.0, 0.0, 11.0, i, 2.0],
      [i, 15.0, 11.0, 0.0, 6.0, i],
      [i, i, i, 6.0, 0.0, 9.0],
      [14.0, i, 2.0, i, 9.0, 0.0]]

g2 = [[0, 1, i, i, i, i, i, i, i],
      [1, 0, 1, i, 1, i, i, i, i],
      [i, 1, 0, 1, i, 1, i, i, i],
      [i, i, 1, 0, i, i, i, i, i],
      [i, 1, i, i, 0, 1, 1, i, i],
      [i, i, 1, i, 1, 0, i, i, 1],
      [i, i, i, i, 1, i, 0, 1, i],
      [i, i, i, i, i, i, 1, 1, i],
      [i, i, i, i, i, 1, i, i, 0]]


print(di.find(g2))
print(fw.find(g2))
print(bf.find(g2))
