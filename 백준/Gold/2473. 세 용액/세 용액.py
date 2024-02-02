n=int(input())
data=list(map(int,input().split()))
data.sort()
result=3000000001
a=()

for i in range(n-2): ## 2개의 요소는 투 포인터
    start , end = i+1 , n-1 ## 매 루프를 돌 때 마다 초기 세팅
    while start < end:
        value = data[i] + data[start] +data[end]
        if abs(result) > abs(value):
            result= value
            a=(data[i],data[start],data[end])

        if value < 0 :
            start+=1
        else:
            end-=1

print(' '.join(map(str,a)))
