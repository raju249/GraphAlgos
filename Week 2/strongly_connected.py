#Uses python3

import sys

sys.setrecursionlimit(200000)



def  DFSUtil(vertex, visited, stack, adj):
    visited.add(vertex)
    for item in adj[vertex]:
        if item in visited:
            continue
        DFSUtil(item, visited, stack, adj)

    stack.append(vertex)

def DFSUtilReverse(vertex, visited, scc, adj2):
    visited.add(vertex)
    scc.add(vertex)
    for item in adj2[vertex]:
        if item in visited:
            continue
        DFSUtilReverse(item, visited, scc, adj2)

def number_of_strongly_connected_components(adj, adj2):
    result = []
    #write your code here
    stack = []
    visited = set()
    for i in range(len(adj)):
        if i in visited:
            continue
        DFSUtil(i, visited, stack, adj)

    visited.clear()

    while stack:
        top = stack.pop()
        if top in visited:
            continue
        scc = set()
        DFSUtilReverse(top, visited, scc, adj2)
        result.append(scc)

    return len(result)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj2 = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj2[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, adj2))
