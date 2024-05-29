N=int(input())
orig=list(map(int,input()))
dest=list(map(int,input()))





def change(idx, li):
    if idx == 0:
        for i in range(2):
            li[idx + i] = 1 - li[idx + i]
    elif idx == N - 1:
        for i in range(-1, 1):
            li[idx + i] = 1 - li[idx + i]
    else:
        for i in range(-1, 2):
            li[idx + i] = 1 - li[idx + i]
    return



# 첫 번째 스위치를 누르지 않는 경우
copy_orig = orig[:]
count1 = 0
for i in range(1, N):
    if copy_orig[i - 1] != dest[i - 1]:
        change(i, copy_orig)
        count1 += 1

# 첫 번째 스위치를 누르는 경우
copy_orig2 = orig[:]
change(0, copy_orig2)
count2 = 1
for i in range(1, N):
    if copy_orig2[i - 1] != dest[i - 1]:
        change(i, copy_orig2)
        count2 += 1



# 결과 계산
if copy_orig == dest:
    result1 = count1
else:
    result1 = float('inf')

if copy_orig2 == dest:
    result2 = count2
else:
    result2 = float('inf')

result = min(result1, result2)

# 결과 출력
if result == float('inf'):
    print(-1)
else:
    print(result)

