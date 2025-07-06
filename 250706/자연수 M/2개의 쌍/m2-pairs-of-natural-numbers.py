# (2,5),(5,8) -> 7,13 => 이 때의 최대는 13
# (5,5),(2,8) -> 10,10 => 이 때의 최대는 10 
# 각 조합에서 나올 수 있는 최댓값을 모두 모은다
# 거기서 최솟값을 찾는다


N=int(input())
nums=[]
ans=0

for _ in range(N):
    x,y=map(int,input().split())
    nums.append((y,x))

nums.sort()


li,ri=0,N-1


while li<=ri:
    ans=max(ans,nums[li][0]+nums[ri][0])

    if nums[li][1] > nums[ri][1]:
        nums[li[1]]-=nums[ri][1]
        ri-=1
    
    elif nums[li][1] < nums[ri][1]:
        nums[ri][1]-=nums[li][1]
        li+=1
    else:
        ri-=1
        li+=1


print(ans)


