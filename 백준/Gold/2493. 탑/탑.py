n=int(input())
a=list(map(int,input().split()))
stack=[]
results=[0 for _ in range(n)]

for i in range(n-1,-1,-1):
    while stack and a[stack[-1]] < a[i]:
        results[stack.pop()]=i+1
    stack.append(i)

for i in results:
    print(i,end=' ')
