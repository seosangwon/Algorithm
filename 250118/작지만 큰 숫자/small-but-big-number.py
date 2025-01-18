from sortedcontainers import SortedSet
n, m = map(int, input().split())
sequence = list(map(int, input().split()))
query = list(map(int, input().split()))
s=SortedSet(sequence)

# Write your code here!

for x in query:
    idx=s.bisect_left(x)
    
    if s[idx]==x and idx!=len(s):
        print(s[idx])
        s.remove(s[idx])
    elif idx>0:
        print(s[idx-1])
        s.remove(s[idx-1])
    else:
        print(-1)

