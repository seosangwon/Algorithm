import sys 
#N개의 물건 , M개의 통로 
N, M = map(int, input().split())
arr = [int(input()) for _ in range(M)]
arr.sort()

# 어떤 노드를 선택할지는 모르지만 최소 시간이 걸려야함 
# 시간 안에 모든 물건이 통과할수있는지 이분탐색을 시작한다 
left=0
right=int(sys.maxsize)

def is_possible(t):
    cnt=0
    for i in range(M):
        cnt+=(time // arr[i])
    
    return cnt>=N


while left<=right:
    time=(left+right)//2 

    if is_possible(time):
        right=time-1
    
    else:
        left=time+1

print(left)


