N=int(input())
balloon=list(map(int,input().split()))


result=0
arrows=[0 for _ in range(1000001)]

for i in range(N):
    if arrows[balloon[i]]==0: # 화살이 해당 위치에 없다면
        result+=1 # 화살 개수를 1개 늘린다
        arrows[balloon[i]-1]+=1 # 높이를 1 낮춘 곳에 화살을 생성한다
    else: # 해당 높이에 화살이 있다면은
        arrows[balloon[i] - 1] += 1  # 높이를 1 낮춘 곳에 화살을 생성한다
        arrows[balloon[i]] -= 1  # 높이가 낮아졌으므로 제 높이에 있던 화살은 제거해준다

print(result)
