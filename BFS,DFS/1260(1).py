import sys

N,M,V = map(int,input().split())
visit = [False] * (N+1) # [[False],[False],[False],[False],[False]]
graph = [[] for _ in range(N+1)]#[[],[],[],[]]




for i in range(M):
    
   S,E = map(int,input().split())
   graph[S].append(E)#간선들을 거꾸로도 왔다리갔다리 할 수 있게 설정해놓음
   graph[E].append(S)
   
   
for i in range(1,N+1):
    graph[i].sort()
     

def DFS(v):
    visit[v] = True
    print(v,end = " ")
    
    for i in graph[v]:
        if not visit[i]:
            DFS(i)
            
DFS(V)
