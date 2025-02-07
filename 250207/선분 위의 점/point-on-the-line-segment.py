import bisect 
n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
# 선분위에 점이 몇개 있는지 구한다 
# 선분에 점을 각각 순회 했을 때 , 그 사이 값이면은 점이 있는 것이다 

for x,y in segments: # 선분 순회 
    answer=0
    line=[x,y]
    for p in points: # 점 순회 
        idx=bisect.bisect_right(line,p)
        if idx==1 or p==line[idx-1]:
            answer+=1
    
    print(answer)
        


