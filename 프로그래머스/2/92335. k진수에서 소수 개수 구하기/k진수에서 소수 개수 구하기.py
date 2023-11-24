def solution(n, k):
    
    answer = 0

    remainder = n // k
    rest = n % k
    # stack으로
    k_result = []
    k_result.append(rest)

    while (remainder > k):
        new_remainder = remainder // k
        rest = remainder % k
        k_result.append(rest)
        remainder = new_remainder

    k_result.append(remainder)

    li=''

    while (k_result):
        value = k_result.pop()
        li+=str(value)


    # 소수인지 판단하는 함수

    def checking(value):
        if value <= 1:
            return 0
        for i in range(2, int(value**0.5) + 1):
            if value % i == 0:
                return 0
        return 1



    int_li=[]

    # 0을 만나면은 지금까지의 값들을 저장 후, 소수 인지 판단
    s = 0
    for i in  range(len(li)):
        if li[i] == '0' :
            val=li[s:i]
            s=i+1
            if val:
                int_li.append(int(val))

        if i ==(len(li)-1):
            val = li[s:i+1]
            if val:
                int_li.append(int(val))

    for value in int_li:
        result=checking(value)
        answer+=result
    
    
    return answer