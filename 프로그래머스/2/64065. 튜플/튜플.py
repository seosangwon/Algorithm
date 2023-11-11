def solution(s):
    answer=[]
    s=s[2:-2]
    s=s.split("},{")
    s_sorted=sorted(s,key=lambda x:len(x))
    for i in s_sorted:
        ii=i.split(",")
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
   


    return answer