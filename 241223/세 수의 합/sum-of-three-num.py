#O(N^2)까지 허용 
from collections import defaultdict
n,k=map(int,input().split())
nums=list(map(int,input().split()))
hash_map=defaultdict(int)
len_=n

for n in nums:
    hash_map[n]+=1

result=0
idx=0
set_nums=set(nums)
for e1 in set_nums:
    for e2 in set_nums:
        e3=k-(e1+e2)
        v1,v2,v3 = hash_map[e1],hash_map[e2],hash_map[e3]
        
        if e1==e2 and e1==e3:
            result+=(v1 *(v2-1) * (v3-2))
            #print(1,e1,e2,e3)
        elif e1==e2 and e2!=e3:
            result+=(v1*(v2-1)*v3)
            #print(2,e1,e2,e3)
        elif e1==e3 and e2!=e3:
            result+=(v1*v2*(v3-1))
            #print(3,e1,e2,e3)
        elif e2==e3 and e1!=e2:
            result+=(v1*v2*(v3-1))
            #print(4,e1,e2,e3)
        elif e1!=e2 and e2!=e3:
            result+=(v1*v2*v3)
            #print(5,e1,e2,e3)


print(result//6)

 