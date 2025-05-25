# N은 최대 5만개
# B가 순서대로 낼 카드가 주어진다 
# A가 얻을 수 있는 최대 점수를 구해라 

N=int(input())
nums=[2]*(2*N +1) # 디폴트는 2로 설정 
nums[0]=0

for _ in range(N):
    n=int(input())
    nums[n]=1


possible=0
answer=0
for i in range(1,2*N+1):
    if nums[i]==1: 
        possible+=1

    
    if nums[i]==2:
        if possible>=1: # possible이 있으면은 값 추가
            answer+=1
            possible-=1
        else: # possible 값이 없으면은 
            continue 

print(answer)



    