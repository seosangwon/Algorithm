# n : 데이터의 크기
n = int(input())

# plus : 양수 데이터 리스트, minus : 음수 데이터 리스트, zero : 0의 개수
plus = []
minus = []
zero_count = 0

result = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    elif num == 0:
        zero_count += 1
    else: # num == 1
        result += num

# 정렬
plus.sort(reverse=True)
minus.sort() # 예: -3 -2 -1 

# 양수 묶기
for i in range(0, len(plus), 2):
    if i+1 < len(plus):
        result += plus[i] * plus[i+1]
    else:
        result += plus[i]

# 음수 묶기 (0이 있으면 마지막 남은 음수를 상쇄)
for i in range(0, len(minus), 2):
    if i+1 < len(minus):
        result += minus[i] * minus[i+1]
    else:
        if zero_count == 0:  # 0이 없으면 마지막 음수를 결과에 추가
            result += minus[i]

print(result)
