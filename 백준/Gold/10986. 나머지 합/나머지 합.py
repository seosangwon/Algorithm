N,M=map(int,input().split())
data=list(map(int,input().split()))
reminder=[0 for _ in range(M)]


sum=0
for i in range(N):
    sum+=data[i]
    reminder[sum%M]+=1

result=reminder[0] # M으로 나누어 떨어지는 구간

for i in range(M):
    result+=reminder[i]*(reminder[i]-1) //2

print(result)



