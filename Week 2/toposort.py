#Uses python3

import sys

def topsortUtil(adj, vertex, stack, visited):
    visited.add(vertex)
    for item in adj[vertex]:
        if item in visited:
            continue
        topsortUtil(adj, item, stack, visited)
    stack.append(vertex)

def toposort(adj):
    visited = set()
    stack = []
    #write your code here
    for i in range(len(adj)):
        if i in visited:
            continue
        topsortUtil(adj, i, stack, visited)
    return reversed(stack)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

