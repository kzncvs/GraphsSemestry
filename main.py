import dijkstra
import floyd_warshall
import bellman_ford

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


print(dijkstra.find(g1))
print(floyd_warshall.find(g1))
print(bellman_ford.find(g1))
