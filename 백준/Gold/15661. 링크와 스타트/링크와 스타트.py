import sys
input=sys.stdin.readline

n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

h=[]
min_value=int(1e9)

def dfs(depth,idx):
    global min_value
    value_A = 0
    value_B = 0
    for i in range(n):
        for j in range(n):
            if i in h and j in h:
                value_A += data[i][j]
            elif i not in h and j not in h:
                value_B += data[i][j]
    diff = abs(value_A - value_B)
    if diff == 0:
        print(0)
        exit()
    else:
        min_value = min(min_value, diff)
    if depth==n//2:
        return

    for i in range(idx,n):
        h.append(i)
        dfs(depth+1,i+1)
        h.remove(i)

dfs(0,0)
print(min_value)
