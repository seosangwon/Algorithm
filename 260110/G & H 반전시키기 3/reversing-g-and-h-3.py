# 한번에 뒤집을 수 있는 최대 크기는 4
# 앞에게 반대여서 뒤집어야 한다 vs 내가 반대여서 뒤집어야 한다. 
# 결국 2번 뒤집는건 의미가 없음
# 내가 반대면은 뒤집는다 최대 4칸까지 봐주면서 뒤집는다. 
# 맞으면 패스 


n=int(input())
a=list(input())
b=list(input())


#변수
answer=0


#함수
def flip(x,n):
    for i in range(4):
        if x+i<n:
            if a[x+i]!=b[x+i]:
                if a[x+i]=='G':
                    a[x+i]='H'
                elif a[x+i]=='H':
                    a[x+i]='G'
            elif a[x+i]==b[x+i]: # 안맞는게 생기면은 바로 끊어야 함 
                break 
        


# 그리디
for i in range(n):
    if a[i]!=b[i]:
        flip(i,n) # 최대 4칸까지 뒤집어주기 
        answer+=1

print(answer)

