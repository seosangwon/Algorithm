# greedy 
# 1. 뒤에서 진행 하되, 지금 내가 0이라면은 무조건 뒤집어야 함 
# 2. 0번째 인덱스의 값이 0이라면 실패 

n=int(input())
a=list(input())
b=list(input())

answer=0

def flip(i):
    for i in range(i,-1,-1):
        if a[i]=='G':
            a[i]='H'
        elif a[i]=='H':
            a[i]='G'


for i in range(n-1,-1,-1):
    if a[i]!=b[i]: # 뒤집어준다 
        flip(i)
        answer+=1
    

print(answer)

