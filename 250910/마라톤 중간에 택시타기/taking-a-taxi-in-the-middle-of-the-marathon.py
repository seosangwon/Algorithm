# 체크포인트 1개만 건너 띈다.
# N의 최대 크기는 1e5 
n=int(input())
x_points=[]
y_points=[]

for _ in range(n):
    x,y=map(int,input().split())
    x_points.append(x)
    y_points.append(y)


# LR 채우기
L=[0]*n
R=[0]*n

for i in range(1,n):
    L[i]=L[i-1]+abs(x_points[i]-x_points[i-1])+abs(y_points[i]-y_points[i-1])

for i in range(n-2,-1,-1):
    R[i]=R[i+1]+abs(x_points[i+1]-x_points[i])+abs(y_points[i+1]-y_points[i])

# 첫 포인트와 끝 포인트는 건너띄기 불가 

answer=int(1e9)
for i in range(1,n-1):
    guri=L[i-1]+R[i+1]+abs(x_points[i+1]-x_points[i-1])+abs(y_points[i+1]-y_points[i-1])
    answer=min(answer,guri)

print(answer)









