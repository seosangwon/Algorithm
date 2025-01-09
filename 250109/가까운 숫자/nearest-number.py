#가장 큰 점 일 때 예외처리
#왼쪽 점과의 거리 , 오른쪽 점과의 거리 구하기
# 만약 이 둘 중에 최소 거리가 나온다면은 minimum 값을 갱신 
from sortedcontainers import SortedSet
n = int(input())
queries = list(map(int, input().split()))
s=SortedSet([0])
answer=queries[0] # 1번째 거리 

for q in queries:
    idx=s.bisect_right(q)
    if idx!=len(s):
        answer=min(answer,s[idx]-q)
    
    idx-=1
    answer=min(answer,q-s[idx])
    s.add(q)
    print(answer)





    


