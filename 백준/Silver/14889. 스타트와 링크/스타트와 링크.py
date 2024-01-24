import sys
input=sys.stdin.readline

n=int(input())
data=[]
ans=int(1e9)
team1=[]

for _ in range(n):
    data.append(list(map(int,input().split())))


def calculate(team1,team2):
    value_team1=0
    value_team2=0
    for i in team1:
        for j in team1:
            value_team1+=data[i][j]
    for i in team2:
        for j in team2:
            value_team2+=data[i][j]
    return abs(value_team1-value_team2)









def dfs(depth,index):
    global ans
    if depth>=n/2:
        team2=[]

        for i in range(n):
            if i not in team1:
                team2.append(i)
    
        value=calculate(team1,team2)
        if ans > value:
            ans=value
        return

    for i in range(index,n):
        if i not in team1:
            team1.append(i)
            dfs(depth+1,i+1)
            team1.remove(i)

dfs(0,0)
print(ans)
