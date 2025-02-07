import bisect
n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# Write your code here!
for x in query:
    idx=bisect.bisect_left(arr,x)
    #print(f"x : {x},idx : {idx} , arr[idx+1]:{arr[idx+1]}")
    if x==arr[idx] :
        print(idx+1)
    if idx==(n-1) or x!=arr[idx] :
        print(-1)
