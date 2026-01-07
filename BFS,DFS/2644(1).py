import sys
from collections import deque


n = int(input())

a,b = map(int(input().split()))
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int(input().split()))
    
    graph[x].append(y)
    graph[y].append(x)
    

visited = [-1] * (n+1)
queue = deque([a])
visited[a] = 0

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if visited[nxt] == -1:
            visited[nxt] = visited[cur] + 1
            queue.append(nxt)
            
print(visited[b])
