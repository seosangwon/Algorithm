data=list(input())
t=int(input())
for _ in range(t):
    alpha,l,r=input().split()
    l=int(l)
    r=int(r)
    sum_data=[0 for _ in range(len(data))]
    if data[0] == alpha:
        sum_data[0]=1

    for i in range(1,len(data)):
        sum_data[i]=sum_data[i-1]
        if data[i]==alpha:
            sum_data[i]+=1

    if l==0:
        print(sum_data[r])
    else:
        print(sum_data[r]-sum_data[l-1])

