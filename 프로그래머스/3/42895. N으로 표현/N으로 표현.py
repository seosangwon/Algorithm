def solution(N, number):
    answer = -1
    
    dp = [set() for _ in range(9)]  # dp[1]부터 dp[8]까지 사용할 수 있도록 크기 9로 설정
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N을 i번 반복해서 만든 숫자 (예: 5, 55, 555, ...)
    
    for i in range(1, 9):
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)  # 덧셈
                    dp[i].add(op1 - op2)  # 뺄셈
                    dp[i].add(op1 * op2)  # 곱셈
                    if op2 != 0:
                        dp[i].add(op1 // op2)  # 나눗셈 (0으로 나누기 방지)
        
        # 현재 dp[i]에 목표 숫자가 있는지 확인
        if number in dp[i]:
            answer = i
            break

    return answer