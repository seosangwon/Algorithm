n, m, l = map(int, input().split())
array = [0]+list(map(int, input().split()))+[l]
array.sort()

start, end = 1, l-1
result = 0
while start <= end:
    count = 0
    mid = (start+end) // 2
    for i in range(1, len(array)):
        # 현재 거리 중 mid보다 큰 거리를 찾아서
        if array[i]-array[i-1] > mid:
            # 나눈 만큼 휴게소를 설치
            count += (array[i]-array[i-1]-1)//mid
    if count > m:
        start = mid+1
    if count <= m:
        end = mid-1
        result = mid
print(result)