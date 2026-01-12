#N의 최대크기는 1e5
# max_value = i-2 번까지의 최대 값 + i+2 번까지의 최대 값  + i 
n=int(input())
arr=list(map(int,input().split()))
L=[0]*n
R=[0]*n
max_l=0
max_r=0

for i in range(n):
    if arr[i]>max_l:
        L[i]=arr[i]
        max_l=L[i]
    else:
        L[i]=max_l

for i in range(n-1,-1,-1):
    if arr[i] > max_r:
        R[i]=arr[i]
        max_r=arr[i]
    else:
        R[i]=max_r

    
answer=0
for i in range(2,n-2):
    value=L[i-2]+R[i+2]+arr[i]

    if answer<value:
        answer=value 
    

print(answer)
        


    
    




