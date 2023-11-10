def solution(answers):
    person1=[1,2,3,4,5]
    person2=[2,1,2,3,2,4,2,5]
    person3=[3,3,1,1,2,2,4,4,5,5]
    solved=[0]*(4)
    answer = []
    
    for i in range(len(answers)):
        index1=i%5
        index2=i%8
        index3=i%10
        if person1[index1]==answers[i]:
            solved[1]+=1
        if person2[index2]==answers[i]:
            solved[2]+=1
        if person3[index3]==answers[i]:
            solved[3]+=1
    max_value=max(solved)
   
    for i in range(1,4):
        if solved[i]==max_value:
            answer.append(i)
    
    return answer