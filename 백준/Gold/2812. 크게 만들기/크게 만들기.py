
N,M=map(int,input().split())
data=list(map(int,input()))

s=[]


for i in range(N):
    while M > 0 and s and s[-1] < data[i]:
        s.pop()
        M -= 1
    s.append(data[i])

# 만약 아직 지워야 할 숫자가 남아있다면 뒤에서부터 제거
if M > 0:
    s = s[:-M]


print(''.join(map(str,s)))

