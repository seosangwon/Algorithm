def find_idx(num, phone):
    for i in range(4):
        for j in range(3):
            if phone[i][j] == num:
                return (i, j)

def solution(numbers, hand):
    answer = ''
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left = (3, 0)
    right = (3, 2)

    for num in numbers:
        if num in (1, 4, 7):
            answer += 'L'
            left = find_idx(num, phone)
        elif num in (3, 6, 9):
            answer += 'R'
            right = find_idx(num, phone)
        else:  # 거리 구해서 가까운 쪽
            x, y = find_idx(num, phone)
            left_d = abs(x - left[0]) + abs(y - left[1])
            right_d = abs(x - right[0]) + abs(y - right[1])

            if left_d < right_d:
                answer += 'L'
                left = (x, y)
            elif right_d < left_d:
                answer += 'R'
                right = (x, y)
            else:
                if hand == 'left':
                    answer += 'L'
                    left = (x, y)
                else:
                    answer += 'R'
                    right = (x, y)

    return answer