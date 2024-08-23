num = int(input())
#최소공배수 최대공약수
for _ in range(num):
    a ,b = map(int, input().split())
    #최소공배수
    for i in range(max(a,b), a*b+1):
        if i % a ==0 and i % b == 0:
            break
    #최대공약수
    for j in range(min(a,b), 0,-1):
        if a % j == 0 and b % j == 0:
            break
    print (i,j)