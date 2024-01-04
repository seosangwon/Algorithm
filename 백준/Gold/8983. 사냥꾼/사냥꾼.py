# 사대의 수 , 동물의 수 , 사정거리
m, n, l = map(int, input().split())
gun=list(map(int,input().split()))
gun.sort()

pigs=[]
for _ in range(n):
    x,y=map(int,input().split())
    pigs.append((x,y))
pigs.sort()

count=0

for p_x,p_y in pigs:
    start=0
    end=m-1
    while start<=end:
        mid=(start+end)//2
        dist=abs(gun[mid]-p_x)+p_y
        if dist <= l:
            count+=1
            break
        if p_x-gun[mid] >=0:
            start=mid+1
        elif p_x-gun[mid]<0:
            end=mid-1

print(count)

