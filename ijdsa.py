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





dfs(a)

if False in visited:
    print('NO')
else:
    print('YES')