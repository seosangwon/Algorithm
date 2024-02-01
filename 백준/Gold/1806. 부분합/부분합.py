import sys
input = sys.stdin.readline

N, S = map(int, input().split())
sequence = list(map(int, input().split()))

prefix = [0] * (N + 1)								
for i in range(1, N + 1):							
    prefix[i] = prefix[i - 1] + sequence[i - 1]		

answer = 100001							
start, end = 0, 1							
while start < N:							
    if prefix[end] - prefix[start] >= S:	
        answer = min(answer, end - start)	
        start += 1							
    else:					
        if end < N:			
            end += 1		
        else:				
            start += 1		

if answer == 100001:		
    answer = 0				
print(answer)