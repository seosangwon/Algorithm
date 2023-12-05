from itertools import combinations
n=int(input())
nums=[]

for i in range(1,11):
    for j in combinations(range(10),i):
        if len(j)==1:
            nums.append(str(j[0]))
        else:
            j=sorted(j,reverse=True)
            value=''.join(map(str,j))
            nums.append(value)


nums.sort(key=lambda x : (len(x),x))

if len(nums) > n :
    print(nums[n])
else:
    print(-1)