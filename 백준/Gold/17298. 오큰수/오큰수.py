n = int(input())
a = list(map(int, input().split()))
results = [-1] * n  # 모든 오큰수를 기본적으로 -1로 초기화
stack = []

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        results[stack.pop()] = a[i]
    stack.append(i)

print(' '.join(map(str, results)))
