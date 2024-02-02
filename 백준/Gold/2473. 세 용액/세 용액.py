n = int(input())
data = list(map(int, input().split()))
data.sort()

closest_sum = float('inf')  # 가능한 가장 큰 수로 초기화
result = []

for i in range(n-2):  # 첫 번째 용액을 고정
    left, right = i+1, n-1  # 두 번째와 세 번째 용액을 위한 포인터
    while left < right:
        current_sum = data[i] + data[left] + data[right]
        
        # 더 작은 합을 찾은 경우 업데이트
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = [data[i], data[left], data[right]]
        
        # 합을 조정하기 위해 포인터 이동
        if current_sum < 0:
            left += 1
        else:
            right -= 1

print(' '.join(map(str, result)))
