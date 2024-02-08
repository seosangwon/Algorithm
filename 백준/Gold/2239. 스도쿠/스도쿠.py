data=[]
zero=[]
zero_len=0
for _ in range(9):
    value=list(map(int,input()))
    data.append(value)

for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            zero.append((i,j))
            zero_len+=1


#행 중복 체크
def width_check(x,value):
    for i in range(9):
        if data[x][i] == value:
            return False
    return True

#열 중복 체크
def height_check( y,value):
    for i in range(9):
        if data[i][y] == value:
            return False
    return True

#3 by 3 사각형 체크
def square_check(x,y,value):
    x= x // 3 * 3
    y= y // 3 * 3
    for i in range(3):
        for j in range(3):
            if data[x+i][y+j]==value:
                return False
    return True



def dfs(index):
    if index == zero_len:
        for i in data:
            print(''.join(map(str,i)))
        exit()
    x,y=zero[index]
    for i in range(1,10):
        if not width_check(x,i):
            continue
        if not height_check(y,i):
            continue
        if not square_check(x,y,i):
            continue
        data[x][y]=i
        dfs(index+1)
        data[x][y]=0

dfs(0)

