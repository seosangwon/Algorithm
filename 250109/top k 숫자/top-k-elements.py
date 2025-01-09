from sortedcontainers import SortedSet

n, k = map(int, input().split())
arr = list(map(int, input().split()))
s=SortedSet(arr)
# Write your code here!

for i in range(k):
    print(s[-(i+1)],end=' ')