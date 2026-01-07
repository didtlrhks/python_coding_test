import sys
sys.setrecursionlimit(int(1e6)) #재귀 깊이제한
input = sys.stdin.readline

def partition(start,end):
    global c, cnt, arr
    pivot = arr[end]
    i = start-1
    for j in range(start,end): 
        if arr[j] <= pivot: #pivot보다 작은 데이터 찾기
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
            cnt += 1
            if cnt == c:
                print(arr[i], arr[j])

    if i+1 != end: #pivot의 위치 변환
        arr[i+1], arr[end] = arr[end], arr[i+1]
        cnt += 1
        if cnt == c:
            print(arr[i+1], arr[end])

    return i+1

def quick_sort(start, end):
    if start >= end:
        return
    q = partition(start, end)
    print(arr)
    quick_sort(start, q-1)
    quick_sort(q+1, end)

if __name__ == "__main__":
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    quick_sort(0, len(arr)-1)
    if c > cnt: print(-1)