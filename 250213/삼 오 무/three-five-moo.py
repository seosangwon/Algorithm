N = int(input())

# N번째로 적히는 숫자를 출력한다 
# 순회하는 방법은 O(N)
left=1
right=int(1e9)

answer=right

def is_possible(k):
    cnt= k - (k//3+k//5 - k//15)

    return cnt


while left<=right:
    mid=(left+right)//2

    if is_possible(mid) >= N :  # 서로 다른 숫자의 개수가 N개 이상이라면은 최소 값을 출력한다 
        right=mid-1
        answer=min(answer,mid)
    else:
        left=mid+1

print(answer)



