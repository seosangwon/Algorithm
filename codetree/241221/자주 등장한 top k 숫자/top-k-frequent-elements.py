# 나온 횟수가 동일하면 값이 더 큰 숫자를 출력한다 
from collections import defaultdict
n,k=map(int,input().split())
nums=list(map(int,input().split()))

hash_map=defaultdict(int)

for n in nums:
    hash_map[n]+=1

order_list=[]

for key , value in hash_map.items():
    order_list.append([key,value])

order_list.sort(key=lambda x: [-x[1],-x[0]])

for i in range(k):
    print(order_list[i][0],end=' ') # key 출력 


