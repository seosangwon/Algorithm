# 같은 구간을 2번 뒤집는거는 사실상 같은행위다 ok 
# 바꿔야 할 부분만 찾아서 뒤집는다는 사실상 위와 같은 풀이인것이다.
# a와 b를 비교하다가 다른 부분이 있으면 체크한다.

N = int(input())
a = list(input())
b = list(input())
answer=0
flag=False # 연속을 체크하는 플래그 변수 

for i in range(N):
    if a[i]!=b[i] and not flag:
        answer+=1
        flag=True
        
    
    if a[i]!=b[i] and flag:
        continue 
    
    
    if a[i]==b[i]:
        flag=False    

print(answer)


