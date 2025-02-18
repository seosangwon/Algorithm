# N의 최대 크기는 1e6
# 배여 값은 음수 일 수도 있다.
import bisect
N=int(input())
arr=list(map(int,input().split()))
INF=-int(1e6)

LIS=[arr[0]]


for num in arr[1:] :
    if LIS[-1] < num: # 제일 큰 값이라면 추가
        LIS.append(num)
    else:
        idx=bisect.bisect_left(LIS,num)
        LIS[idx]=num


print(len(LIS))



