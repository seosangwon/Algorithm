import bisect

def LIS_find(prices):
    LIS=[]
    for price in prices:
        pos=bisect.bisect_left(LIS,price)
        if pos == len(LIS): #현 LIS에서 제일 큰 값 이라면 
            LIS.append(price)
        else: # 좀 더 작은 값이 그 자리를 대체 해버림 [1,4,5] -> [1,3,5]
            LIS[pos]=price
       

    return len(LIS)





while True:
    try:
        n=int(input())
        data=list(map(int,input().split()))
        print(LIS_find(data))


    except EOFError:
        break

