n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
answer=int(1e9)
left,right=0,0

cur_sum=arr[0]
while left<=right and right<n-1 :
    #print(left,right,cur_sum)
    if cur_sum<s : # 현재의 합이 s보다 작은경우 right를 1칸 늘려야 한다 
        right+=1
        cur_sum+=arr[right]
        
    
    else : # 현재의 합이 s보다 같거나 큰경우 answer를 갱신해주고 left를 1칸 늘린다 
        #print(left,right)
        answer=min(answer , (right-left)+1)
        cur_sum-=arr[left]
        left+=1
        
        

if answer==int(1e9):
    print(-1)
else:
    print(answer)



    

