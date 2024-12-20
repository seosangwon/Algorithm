#시간복잡도 : O(nlogn)
from collections import defaultdict
n,k=map(int,input().split())
nums=list(map(int,input().split()))
answer=0
hash_map=defaultdict(int)

for n in nums:
    hash_map[n]+=1

for n in set(nums):
    r=k-n
    if n==r: # 값이 같을 경우 
        answer+=hash_map[n] * (hash_map[r]-1)
    else:
        answer+=hash_map[n]*hash_map[r]

print(answer//2)




    
        

