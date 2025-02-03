from collections import deque
n = int(input())
arr = list(map(int, input().split()))


# 시간복잡도 n은 최대 1e5
# 구각 내의 중복되는 숫자가 없는지 어떻게 확인할것인가??
# in 연산자 써서 arr[right]의 값이 couting_array에 있으면은 arr[left]값을 제거 하고 left+=1 없으면은 갱신 
answer=1
left,right=0,0
count_arr=deque([arr[0]])
while left<=right and right<n-1:
    right+=1
    
    if arr[right] in count_arr: # 있으면은 left 값 제거 
        idx=count_arr.index(arr[right]) # 중복된 원소에 idx 찾기 
        
        for i in range(idx+1):
            count_arr.popleft()
            left+=1
        
    
    else:
        answer=max(answer , right-left+1)
    
    count_arr.append(arr[right])
    
    


print(answer)
        




