#자동차를 단 한 번 사서 팔 수 있다. 
#N은 최대 10만개
n = int(input())
price = list(map(int, input().split()))
answer=0
min_value=price[0]

for i in range(1,n):
    if price[i] - min_value > 0 : # 팔 수 있다면은 갱싱 
        answer=max(answer , price[i]-min_value)
    
    min_value=min(min_value,price[i]) # 최솟 값은 매번 갱신 

print(answer)






