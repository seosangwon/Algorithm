from sortedcontainers import SortedSet
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
s=SortedSet(arr)

# Write your code here!
# 숫자가 대입 될 때 , x - 나보다 작거나 같은수 >=m , 나보다 같거나 큰 수 - x >=m 
answer=int(1e9)
for x in arr:
    left_idx=s.bisect_left(x+m) 
    if left_idx != len(s): # 같은 수가 있으면 괜찮은데 이게 만약 제일 큰 수라면은 arr에 없는 원소 인것이다.
        answer=min(answer,s[left_idx]-x)
    
    right_idx=s.bisect_right(x-m)
    if right_idx>0:
        answer=min(answer,x-s[right_idx-1])


if answer==int(1e9):
    answer=-1

print(answer)





