from sortedcontainers import SortedSet
n, m = map(int, input().split())
queries = list(map(int, input().split()))

s=SortedSet([i for i in range(1,m+1)])


# Write your code here!
for q in queries:
    s.remove(q)
    print(s[-1])
