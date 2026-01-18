import sys

n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
result = []
current = 1

for x in sequence:
    # x가 나올 때까지 push
    while current <= x:
        stack.append(current)
        result.append("+")
        current += 1

    # 스택 top이 x면 pop
    if stack and stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        sys.exit()

# 가능하면 연산 출력
print("\n".join(result))
