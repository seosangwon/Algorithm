N,K=map(int,input().split())
data=list(map(int,input().split()))

hash_map={0:1}
sum_=0
answer=0

for i in data:
    sum_+=i

    if sum_-K in hash_map.keys():
        answer+=hash_map[sum_-K]

    hash_map[sum_]=hash_map.get(sum_,0)+1

print(answer)


