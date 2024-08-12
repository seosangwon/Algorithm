def recursion(start_x , start_y , size):
    if size==1: # 더 이상 못 나눌때 까지
        return
    # conquer : 가운데 구멍 내기
    new_size = size // 3
    for i in range(start_x+new_size , start_x+new_size*2): # 9 ~ 17
        for j in range(start_y + new_size, start_y + new_size * 2):
            data[i][j]=" "


    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            recursion(start_x + i * new_size,start_y + j*new_size , new_size)






N=int(input())
data=[["*" for _ in range(N)] for _ in range(N)]


#divide
recursion(0,0,N)


for i in range(N):
    for j in range(N):
        print(data[i][j],end='')
    print()