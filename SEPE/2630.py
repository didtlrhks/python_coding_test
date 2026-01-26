import sys

input = sys.stdin.readline


N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]

white = 0
blue = 0

def slic(x,y,size):
    global white , blue
    color = paper[x][y]
    
    for i in range(x,x + size):
        for j in range(y,y + size):
            if paper[i][j] != color:
                half = size//2
                slic(x,y,half)
                slic(x,y+half,half)
                slic(x+half,y,half)
                slic(x+half,y+half,half)
                return
            
            
    if color == 0 :
        white +=1
    else:
        blue+=1
        
slic(0,0,N)
print(white)
print(blue)                
                
            
        
    
    
    