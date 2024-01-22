def width_check(x, value):
    for i in range(9):
        if value == data[x][i]:
            return False
    return True


def height_check(y,value):
    for i in range(9):
        if value == data[i][y]:
            return False
    return True


def square_check(x,y,value):
    for i in range(3):
        for j in range(3):
            if value == data[(x//3)*3 +i][(y//3)*3 +j]:
                return False
    return True


data=[]
pos_0=[]
visited=[False for _ in range(len(pos_0))]

for i in range(9):
    data.append(list(map(int,input().split())))
    for j in range(9):
        if data[i][j]==0:
            pos_0.append((i,j))




def dfs(index):

    if index==len(pos_0):
        for i in range(9):
            print(' '.join(map(str,data[i])))

        exit()

    x, y = pos_0[index]


    for i in range(1,10):
        if width_check(x, i) and height_check(y, i) and square_check(x, y, i):
            data[x][y]=i
            dfs(index+1)
            data[x][y] = 0 #실패 했다면 이 코드가 실행된다






dfs(0)
print(data)
