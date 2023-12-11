from itertools import permutations

n=int(input())
data=list(input().split())



value=[0,1,2,3,4,5,6,7,8,9]

per_value=list(permutations(value,n+1))
results=[]

for li in per_value:
    result=[]
    result.append(str(li[0]))
    for i in range(n):
        a=li[i]
        b=li[i+1]
        comp=data[i]
        if comp == '<':
            if a < b :
                result.append(str(b))
            else:
                break
        elif comp == '>':
            if a > b:
                result.append(str(b))
            else:
                break
    if len(result) == n+1:
        results.append((''.join(result)))

print(results[-1])
print(results[0])

# print(results)
