import sys

input = sys.stdin.readline
# 바로 옆에 있는게 나랑 같으면 나포함 다음걸 같이 삭제

T = int(input())

for _ in range(T):
    s = input()
    stack = []
    vaild = True
    
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                valid = False
                break
            stack.pop()
            
    if stack:
        valid = False
      
      
    if valid == True:
        print("YES")
    if valid == False:
        print("NO")  
    
        
                

