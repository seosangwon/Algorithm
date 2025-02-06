n = int(input())
a = list(map(int, input().split()))

# Write your code here!
#투포인터로 하다가 부분합이 음수가 되면은 끊는다 
left,right=0,0
answer=-int(1e9)
sum_=0
while left<=right and right < n:
    sum_+=a[right] # 새로운 값 추가 
    answer=max(answer, sum_) # 갱신

    if sum_ >0 : 
        right+=1
    if sum_ <=0 : # 부분 합이 음수가 된다면 새로운 투포인터로 끊기
        left=right+1
        right+=1
        sum_=0 # 총합 초기화 

print(answer)