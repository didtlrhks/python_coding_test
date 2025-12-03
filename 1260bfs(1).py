from collections import deque

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)

for i in range(N+1):
    S,E = map(int,input().split())
    graph[S].append(E)
    graph[E].append(S)
    
    
def BFS(v):
    queue = deque([v])
    visit[v] = True
    
    while queue:
        x = queue.popleft()
        print(x,end = " ")
        
        for i in graph[x]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)
                
BFS(V)