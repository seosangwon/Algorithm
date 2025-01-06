#친한 점 기준 : x<x' or (x=x' and y<=y')
from sortedcontainers import SortedSet
n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

s=SortedSet(points)

# Write your code here!

for x,y in queries:
    idx=s.bisect_right((x,y))
    if idx >=n:
        print(-1,-1)
    else:
        print(s[idx][0],s[idx][1])

