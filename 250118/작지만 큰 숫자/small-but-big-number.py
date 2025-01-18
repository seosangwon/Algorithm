from sortedcontainers import SortedSet
n, m = map(int, input().split())
sequence = list(map(int, input().split()))
query = list(map(int, input().split()))
s=SortedSet(suquence)

# Write your code here!

for x in query:
    idx=s.bisect_left(x)
    idx-=1

    if idx>0:
        print(s[idx])
        remove(s[idx])
    else:
        print(-1)

