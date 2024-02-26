n=int(input())
data=[]

for _ in range(n):
    data.append(list(map(int,input().split())))

white=0
blue=0


def divide_conquer(x,y,n):
    global white , blue
    color=data[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if data[i][j]!=color:
                divide_conquer(x,y,n//2)
                divide_conquer(x, y+n//2, n // 2)
                divide_conquer(x+n//2, y, n // 2)
                divide_conquer(x+n//2, y+n//2, n // 2)
                return 


    if color==1:
        blue+=1
    else:
        white+=1

divide_conquer(0,0,n)
print(white)
print(blue)
