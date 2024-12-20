#시간복잡도 : O(nlogn)
n,k=map(int,input().split())
nums=list(map(int,input().split()))
hash_map={}
answer=0
min_num=min(nums)
max_num=max(nums)

#전부 0으로 초기화
for n in range(min_num , max_num+1):
    hash_map[n]=0

#딕셔너리에 갯수 추가 
for n in nums:
    hash_map[n]+=1

#중복 값 제거 
nums_set=set(nums)

for n in nums_set:
    r=k-n
    if min_num <= r <= max_num:
        answer+=hash_map[n]*hash_map[r]
    
        
    
print(answer//2)
        
    
        

