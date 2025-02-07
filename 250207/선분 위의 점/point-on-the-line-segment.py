import bisect 
n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
# 선분위에 점이 몇개 있는지 구한다 

for x,y in segments: # 선분의 시작과 끝 순차 조회 
    x_idx=bisect.bisect_left(points,x)
    y_idx=bisect.bisect_right(points,y)
    
    answer = y_idx - x_idx
    print(answer)





