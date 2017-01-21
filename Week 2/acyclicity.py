#Uses python3

import sys

adjacent = []

def acyclic(adj):
    global adjacent
    white_set = []
    gray_set = []
    black_set = []
    adjacent = adj
    for i in range(len(adj)):
        white_set.append(i)

    for item in white_set:
        current = item
        if dfs(current, white_set, gray_set, black_set):
            return 1
    return 0

def dfs(current, white_set, gray_set, black_set):
    move_vertex(current, white_set, gray_set)

    for vertex in adjacent[current]:
        if vertex in black_set:
            continue

        if vertex in gray_set:
            return True

        if dfs(vertex, white_set, gray_set, black_set):
            return True

    move_vertex(current, gray_set, black_set)
    return False


def move_vertex(vertex, source, destination):
    source.remove(vertex)
    destination.append(vertex)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
