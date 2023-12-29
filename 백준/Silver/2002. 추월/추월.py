n=int(input())
in_car={}
for i in range(1,n+1):
    in_car[input()]=i

out_car=[]
for _ in range(n):
    out_car.append(input())

count=0
for i in range(n-1):
    for j in range(i,n):
        if in_car[out_car[i]] > in_car[out_car[j]]:
            count+=1
            break

print(count)
