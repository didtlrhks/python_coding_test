

N,M,V = map(int,input().split())


graph = [[] for _ in range(N+1)]


for _ in range(M):
    S,E = map(int,input().split())
    graph[S].append(E)
    graph[E].append(S)
    

for i in range(1,N+1):
    graph[i].sort()
    
visit = [False] * (N + 1)

def DFS(v):
    visit[v] = True
    print(v,end= ' ')
    
    for i in graph[v]:
        if not visit[i]:
            DFS(i)
            

visit = [False] * (N+1)

    def BFS(v):
        queue = deque([v])
        visit[v] = True 
        
        while queue:
            x = queue.popleft()
            print(x, end = ' ')
            
            for i in graph[x]:
                if not visit[i]:
                    visit[i] = True
                    queue.append(i)
                    

DFS(V)
BFS(V)
       