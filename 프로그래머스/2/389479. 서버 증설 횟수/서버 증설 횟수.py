# 한번 증설한 서버는 k시간 동안 운영하고 반납합니다
# (n*m)명 이상시 서버 증설이 필요하다 
# 현 시간에서 몇 명의 사용자를 받아들일 수 있는지 체크 해야 함 
# 0시에서 23시까지 리스트를 받는다 
# 증설된 서버의 수 리스트도 필요 
def solution(players, m, k):
    answer = 0
    cur_server=[1]*(24)
    
    for i in range(24):
        if players[i] >= m*cur_server[i]: # 현재 서버가 감당 할 수 없다면은 추가 서버 증진 
            p = (players[i] - m * cur_server[i])
            plus_server=p//m + 1
            
            for j in range(k): # 서버 증설 
                if i+j <= 23:
                    cur_server[i+j]+=plus_server
            answer+=plus_server
    print(cur_server)
    

    
    return answer