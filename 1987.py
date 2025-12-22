import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


R,C = map(int,input().split())
board = [list(input().strip()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

used = [False] * 26
answer = 0



def dfs(x,y,cnt):
    global answer
    answer = max(answer,cnt)
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < R and 0 <= ny < C:
            idx = ord(board[nx][ny]) - ord('A')
            
        
        