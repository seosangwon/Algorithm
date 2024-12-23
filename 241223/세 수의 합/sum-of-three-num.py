#O(N^2)까지 허용 
from collections import defaultdict
n,k=map(int,input().split())
nums=list(map(int,input().split()))
hash_map=defaultdict(int)

for n in nums:
    hash_map[n]+=1

result=0
for e1 in nums:
    for e2 in nums:
        e3=k-(e1+e2)
        v1,v2,v3 = hash_map[e1],hash_map[e2],hash_map[e3]
        
        if e1==e2 and e1==e3:
            result+=(v1 *(v2-1) * (v3-2))
        elif e1==e2 and e2!=e3:
            result+=(v1*(v2-1)*v3)
        elif e1==e3 and e2!=e3:
            result+=(v1*v2*(v3-1))
        elif e2==e3 and e1!=e2:
            result+=(v1*v2*(v3-1))
        elif e1!=e2 and e2!=e3:
            result+=(v1*v2*v3)

print(result//12)

 