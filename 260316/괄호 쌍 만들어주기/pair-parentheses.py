# A의 최대 길이는 1e5
# 왼쪽쌍 개수를 나타내는 리스트 1개 필요
# answer: 순회하면서 i번째에 오른쪽 쌍 2개가 연속으로 나왔다면 i * L[i]를 더하다. 
A=list(input())
n=len(A)
L=[0]*n

for i in range(1,n):
    if A[i-1]=='(' and A[i]=='(':
        L[i]=L[i-1]+1
    else:
        L[i]=L[i-1]


answer=0

for i in range(1,n):
    if A[i-1]==')' and A[i]==')': # 조건성립
        answer+=L[i] 

print(answer)






