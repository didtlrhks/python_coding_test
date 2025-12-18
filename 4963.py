import sys
from collections import deque



dw = [-1,1,-1,0,0,1,1,1]
dh = [-1,0,1,-1,1,-1,0,1]

def BFS(w,h,graph,visit):
    queue = deque()
    queue.append((w,h))
    
    visit[h][w] = True
    
    while queue:
        w,h = queue.popleft()
        
        for i in range(8):
            nw = w + dw[i]
            nh = h + dh[i]
        
            if 0 <= nw < W and 0<= nh < H:
                if not visit[nh][nw] and graph[nh][nw] == 1:
                    visit[nh][nw] = True
                    queue.append((nw,nh))
                    count += 1


while True:
    

    W,H = map(int,input().split())
    if W == 0 and H == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(H)]
    visit = [[False]*W for _ in range(H)]
    count = 0
    
    for h in range(H):
        for w in range(W):
            if graph[h][w] == 1 and not visit[h][w]:
                BFS(w,h,graph,visit,W,H)
                count+=1
                
    print(count)