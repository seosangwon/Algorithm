n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def dragon_curb(x,y,d,g):
    directions=[d]
    points=[(x,y)]
    for _ in range(g):
        directions+=[(i+1)%4 for i in reversed(directions)]

    for d in directions:
        if d==0:
            x+=1
        elif d==1:
            y-=1
        elif d==2:
            x-=1
        elif d==3:
            y+=1
        points.append((x,y))

    return points

def square(data):
    result=0
    for i in range(100):
        for j in range(100):
            if data[i][j]==1 and data[i+1][j]==1 and data[i][j+1]==1 and data[i+1][j+1]==1:
                result+=1

    return result



#main
data=[[0 for _ in range(101)] for _ in range(101) ]


for x,y,d,g in graph:
    p=dragon_curb(x,y,d,g)

    for x,y in p:
        data[x][y]=1

print(square(data))
