# n,m : 의자에 대한 정보  n개 , 의자의 수 m개 
# add를 하기 전에 bisect_rigt의 idx가 길이값과 같으면은 그것은 제일 큰 수이다 
from sortedcontainers import SortedSet
n, m = map(int, input().split())
a = list(map(int, input().split()))
s=SortedSet( range(1,m+1))

# Write your code here!
answer=0
for e in a:
    idx=s.bisect_right(e)
    if idx !=0:
        idx-=1
        answer+=1
        s.remove(s[idx])
    else:
        break

print(answer)
    