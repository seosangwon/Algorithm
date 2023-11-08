def solution(s):
    words=["zero","one","two","three","four","five","six","seven","eight","nine"]
    check=""
    result=[]
    for i in s:
        if "0"<=i<="9":
            result.append(i)
        else:
            check+=i
            if check in words:
                value=words.index(check)
                result.append(str(value))
                check=""
    
    
    
    answer="".join(result)
    answer=int(answer)
    return answer