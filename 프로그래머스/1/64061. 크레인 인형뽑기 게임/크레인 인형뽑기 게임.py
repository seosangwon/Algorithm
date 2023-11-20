def solution(board, moves):
    answer = 0
    basket=[]
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] ==0 :
                continue
            else:
                #새로뽑은 인형과 stack의 top이 같은 인형일 경우
                if basket and board[j][i-1] == basket[-1]:
                    basket.pop(-1)
                    answer+=2
                    board[j][i-1]=0
                else: #stack에 쌓아주기
                    basket.append(board[j][i-1])
                    board[j][i-1]=0
                break
             
    return answer