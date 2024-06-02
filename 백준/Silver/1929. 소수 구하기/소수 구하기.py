M,N=map(int,input().split())
data=[i for i in range(N+1)]

#예외상황들
if M==1:
    M=2

flag=False
for i in range(2,int(N**0.5)+1):
    j=2

    while i*j <=N:
        if data[i*j] !=0:
            data[i*j]=0
            
        j+=1




for i in range(M,N+1):
    if data[i]!=0:
        print(i)

