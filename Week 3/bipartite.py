#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    queue = []
    queue.append(0)
    color = [-1 for _ in range(len(adj))]
    color[0] = 1
    while queue:
        u = queue.pop(0)
        for vertex in adj[u]:
            if color[vertex] == -1:
                color[vertex] = 1 - color[u]
                queue.append(vertex)
            elif color[vertex] == color[u]:
                return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
