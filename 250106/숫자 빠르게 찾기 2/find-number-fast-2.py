from sortedcontainers import SortedSet
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]
s=SortedSet(arr)

# Write your code here!

for q in queries:
    idx=s.bisect_left(q)
    if idx >=n:
        print(-1)
    else:
        print(s[idx])

