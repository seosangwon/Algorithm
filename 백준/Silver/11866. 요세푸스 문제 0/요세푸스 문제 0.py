n,k=map(int,input().split())

nums=list(i for i in range(1,n+1))
idx=k-1
answer=[]

while nums:
    idx%=n
    answer.append(nums[idx])
    del nums[idx]
    idx-=1
    idx+=k
    n-=1

result = "<" + ", ".join(map(str,answer))+">"
print(result)