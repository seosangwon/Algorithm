import sys
input=sys.stdin.readline

n=int(input())
broken_num=int(input())
broken_button=list(map(int,input().split()))




minimum=abs(100-n)

for i in range(1000001):
    i=str(i)
    for j in range(len(i)):
        if int(i[j]) in broken_button:
            break
        #모든 버튼이 동작가능하다면은
        elif j==len(i)-1:
            minimum=min(minimum,abs(int(i)-n)+len(i))

print(minimum)




