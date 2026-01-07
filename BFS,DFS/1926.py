import sys
from collections import deque


n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

max_area = 0
count = 0



    
def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    visit[x][y]
    area = 1
    
    while queue:
        cx,cy = queue.popleft()
        
         for i in range(4):
             nx = cx + dx[i]
             ny = cy + dy[i]
         
            
             if 0 <= nx < n and 0 <= ny < m:
                 if graph[nx][ny] == 1 and visit[nx][ny] == 0:
                     visit[nx][ny] == 1
                     queue.append((nx,ny))
                     arear += 1
    return area

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visit[i][j] == 0:
            count += 1
            max_area = max(max_area, BFS(i,j))
            
print(count)
print(max_area)
        

            
    
    
    
    # 입력하고
    # 그래프를 만들고
    # 주변이 다 0인지 아닌지 주변이 다 0 이면 끝, 그리고 그림하나 카운트올리고
    # 1의개수 판별해서 answer 에다가 넣고 다끝나고 이중에 가장큰거 리턴
    