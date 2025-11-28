

N,M = (map(int,input().split()))
array = []

def backtracking():
    if len(array) == M:
        print(" ".join(map(str,array)))
        return
    for i in range(1,N+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()
            
backtracking()
    
    
    N , M = map(int,input().split())
    array = []
    backtracking()
    
    def backtracking():
        if len(array) == M:
            print(" ".join(map(str,array)))
            return
        for i in range(1,N+1):
            if i not in array:
            array.append(i)
            backtrancking()
            array.pop()
            
            
            