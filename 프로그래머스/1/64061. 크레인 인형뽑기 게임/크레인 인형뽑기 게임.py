def solution(board, moves):
    answer = 0
    stack=[]
    N=len(board[0])
    answer=0
    for idx in moves:
        idx-=1 # 1X1 시작이므로 1빼고 시작 
        value=0 # 뽑기 값
        for i in range(N):# 행만 움직이면 됨
            if board[i][idx]==0: # 비어있으면 pass
                continue
            else: # 값이 있으면
                value=board[i][idx]
                board[i][idx]=0
                break # 뽑았으면 멈추기 
        
        if value==0: # 아예 빈 열이였으면 pass
            continue
        
        if stack: # stack에 값이 있다면
            prev=stack[-1] # 이전 값은 stack의 최상단 값
            if prev==value:
                answer+=2
                stack.pop()
            else:
                stack.append(value)
        else: # stack에 값이 없거나 , 애니팡이 안된다면
            stack.append(value)
        
        
        
#         for i in range(N): # 디버깅
#             for j in range(N):
#                 print(board[i][j],end=' ')
#             print()
#         print()
            

    return answer