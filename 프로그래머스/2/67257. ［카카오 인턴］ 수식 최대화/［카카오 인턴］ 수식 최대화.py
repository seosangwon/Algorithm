from itertools import permutations

def solution(expression):
    li = []
    operators = []
    num_str = ""
    
    # 부호 / 숫자 구분하기 
    for e in expression:
        if e in "-+*":
            li.append(int(num_str))
            li.append(e)
            if e not in operators:
                operators.append(e)
            num_str = ""
        else:
            num_str += e
    li.append(int(num_str))  # 마지막 숫자 추가
    
    # 연산자 우선순위 순열 생성
    operator_permutations = list(permutations(operators))
    
    def calculate(v1, v2, o):
        if o == '+':
            return v1 + v2
        elif o == '-':
            return v1 - v2
        elif o == '*':
            return v1 * v2
    
    max_value = 0
    for order in operator_permutations:
        nums = li[:]  # 복사
        for op in order:  # 연산자 우선순위에 따라 계산
            while op in nums:
                idx = nums.index(op)
                result = calculate(nums[idx-1], nums[idx+1], op)
                
                nums = nums[:idx-1] + [result] + nums[idx+2:]
        
        max_value = max(max_value, abs(nums[0]))
    
    return max_value