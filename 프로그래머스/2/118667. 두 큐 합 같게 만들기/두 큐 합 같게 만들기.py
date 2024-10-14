# 출력 조건 : 두 큐의 합을 같게만드는 작업의 최소 횟수를 출력
# 시간복잡도 : 각 큐의 최대 길이는 3e5
# 각 원소별로 남느냐 , pop 되냐 : 2가지의 선택지가 존재 
# 알고리즘 : 투포인터
# 1. q1,q2를 합친다
# 2. 투 포인터로 계싼 
# 3. 투 포인터 안에 있는 수 == 그 외에 수 들이 같으면 맞음
# 4. 투 포인터의 합이 전체 //2 보다 작으면 right+=1 , 크면 left+=1 
# 5. left > right 되면은 -1 return 
# 6. 1턴이 지날때마다 cnt +=1

def solution(queue1, queue2):
    answer = -1
    q=queue1+queue2
    n=len(q)
    left=0
    right=n//2-1
    total_sum=sum(q)
    target=total_sum//2
    sum_=sum(q[left:right+1])
    
    cnt=0
    
    while left<= right and right<n:
        
        
        if sum_==target:            
            return cnt
        elif sum_ < target:
            right+=1
            if right<n:
                sum_+=q[right]
        else:
            sum_-=q[left]
            left+=1
            
        
        cnt+=1
            
            
    
    return answer