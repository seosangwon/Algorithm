n=int(input())
lines=[]

for _ in range(n):
    a,b=map(int,input().split())
    lines.append((a,b))


lines=sorted(lines,key = lambda x:x[0])
b_sequence=[line[1] for line in lines]


#각 idx에서 LIS를 구한다
def LIS(sequence):
    dp=[1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

v=LIS(b_sequence)
print(n-v)
