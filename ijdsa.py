n, m = map(int, input().split())
graph = {}
if n == 1:
    print('YES')
    exit()
elif m == 0:
    print('NO')
    exit()

for i in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)
visited = [False] * n


def dfs(u, prev=0):
    visited[u - 1] = True
    for v in graph[u]:
        if not visited[v - 1]:
            dfs(v, u)
        elif v != prev:
            print('NO')
            exit()


dfs(a)

if False in visited:
    print('NO')
else:
    print('YES')