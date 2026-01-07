import sys
from collections import deque

N = int(input())
graph = [list(input().stripe()) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = [] 



def BFS(x,y):
    queue = deque()
    queue.append(x,y)
    count = 1
    visit[x][y] = True
   
    
    
while queue:
    x,y = queue.popleft()
    queue.append((x,y))
    
    
    for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < N and 0 <= ny < N:
        if not visit[nx][ny] and graph[nx][ny] == '1':
            queue.append((nx,ny))
            visit[nx][ny] = True
            count += 1
            
return count
  
  

for i in range(N):
    for j in range(N):
        if not visit[i][j] and graph[i][j] == '1':
            result.append(BFS(i,j))
            


   result.sort()
   
print(len(result))   
for r in result:
    print(r)
    
     

              
              
    
    
    
    
    
    
    
    