N = int(input())

# N번째로 적히는 숫자를 출력한다 
# 순회하는 방법은 O(N)
num=1
for i in range(N-1):
    num+=1
    while num%3 == 0 or num % 5==0:
        num+=1
    
        

print(num)
    
    




