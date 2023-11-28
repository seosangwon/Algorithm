from itertools import combinations

n,m=map(int,input().split())
data=list(map(int,input().split()))
data.sort(reverse=True)

data_comb=list(combinations(data,3))
sum_list=[]

for i in data_comb:
  comb_sum=sum(i)
  sum_list.append(comb_sum)
  

sum_list.sort(reverse=True)

result=0
for i in sum_list:
  if i <= m:
    result=i
    break

print(result)
  