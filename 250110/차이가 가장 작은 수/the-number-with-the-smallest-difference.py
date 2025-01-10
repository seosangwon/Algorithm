from sortedcontainers import SortedSet
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
s=SortedSet([arr[0]])
# Write your code here!
answer=int(1e9)

for e in arr[1:]:
    idx=s.bisect_right(e)
    if idx!=len(s):
        r_value=s[idx]-e
        if r_value >=m:
            answer=min(answer,r_value)
    
    idx-=1
    l_value=e-s[idx]
    if l_value>=m:
        answer=min(answer,l_value)
    s.add(e)

if answer==int(1e9):
    answer=-1

print(answer)


