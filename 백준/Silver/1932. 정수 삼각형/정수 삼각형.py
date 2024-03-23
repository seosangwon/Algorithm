n=int(input())
data=[list(map(int,input().split()))for _ in range(n)]




#0열이라면 위 , 맨 오른쪽 끝 열 이라면 왼쪽 위 , 나머지는 왼쪽 위 & 위 : 3가지 경우의 수


for i in range(1,n):
  for j in range(i+1):
    if j==0:
      data[i][j]+=data[i-1][j]
    elif j==i:
      data[i][j]+=data[i-1][j-1]
    else:
      data[i][j]=max(data[i][j]+data[i-1][j-1] ,data[i][j]+data[i-1][j])
    

result=0
for i in range(n):
  result=max(result,data[n-1][i])
print (result)