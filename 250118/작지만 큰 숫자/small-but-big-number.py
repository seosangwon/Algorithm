from sortedcontainers import SortedSet
n, m = map(int, input().split())
sequence = list(map(int, input().split()))
query = list(map(int, input().split()))
s=SortedSet(sequence)

# Write your code here!

for x in query:
    idx=s.bisect_right(x) # x보다 큰 수 반환 
    
    if idx >0: # 본인이 제일 작은수가 아니라면은 
        print(s[idx-1])
        s.remove(s[idx-1])
    else:
        print(-1)

