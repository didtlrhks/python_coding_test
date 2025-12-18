import sys
from collections import deque



W,H = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(H)]
count = 0

dx = [-1,1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def BFS(w,h,graph,visit):
    queue = deque()
    queue.append((w,h))
    
    visit[w][h] = True
    
    while queue:
        w,h = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < N and 0<= ny < N:
                if not visit[nx][ny] and graph[nx][ny] == False:
                    visit[nx][ny] == True
                    queue.append((nx,ny))
                    count += 1
    return count

           


        
        
    
