n=int(input())
data=[[0 for _ in range(101)] for _ in range(101)]

# 사각형에 1채워넣기
for _ in range(n):
    x,y=map(int,input().split())
    # x,y 좌표계를 행렬로 바꾸자
    # (3,7) -> (100-(y+10) , x)

    n=100-(y+10)
    m=x

    for i in range(10):
        for j in range(10):
            data[n+i][m+j]=1

# 사각형 세로 기준으로 누적합 계산하기
for i in range(1,100):
    for j in range(1,101):
        if data[i][j]>0:
            data[i][j]+=data[i-1][j]

#출력 확인
# for i in range(101):
#     for j in range(101):
#         print(data[i][j],end=' ')
#     print()

max_area=0
#사각형 넓이 계산
for i in range(1,101):
    for j in range(1,101):
        if data[i][j] > 0:
            height=data[i][j]
            for width in range(1,101-j):
                if data[i][j+width-1] < height:
                    height=data[i][j+width-1]
                if height == 0 :
                    break

                max_area=max(max_area , height* width)

print(max_area)



