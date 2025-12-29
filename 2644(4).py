import sys
from collections import deque

n = int(input())

q,w = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]


for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
    
visited = [-1] * (n+1)
queue = deque([a])
visited[q] = 0

while queue:
    cur = deque.popleft()
    for i in garph[cur]:
        if visited[i] == -1:
            visited[i] = visited[cur] + 1 
            queue.append(i)
            
print(visited[w])
            
        
    
    
    
    
    
    