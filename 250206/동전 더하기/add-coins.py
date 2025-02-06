n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Write your code here!
answer=0
idx=n-1
while k!=0:
    if k >= coins[idx]: #현재 값으로 나눌 수 있는 경우
        answer+=1
        k-=coins[idx]
    else: # 나눌 수 없는 경우
        idx-=1

print(answer)
