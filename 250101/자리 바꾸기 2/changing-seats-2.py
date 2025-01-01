# 1번 ~ N번은 순서대로 자리에 앉아있다
# K분 동안 K번 자리를 바꾼다 
# 3K 까지 반복 
# 각 사람들은 몇번의 자리를 앉을 수 있었는지 출력해라 
# 1. 각 번호별로 set 만들기
# 2. 움직여지면은 set 자료구조에 추가하기 

N,K=map(int,input().split())
current_sit=[i for i in range(N+1)] # 현재 좌석 배치 
sit_list=[set()  for _ in range(N+1)] # 각 사람별 좌석 이용 내역

for i , sit_set in enumerate(sit_list):
    sit_set.add(i)


cmd_list=[] # 명령어 리스트 

for _ in range(K):
    a,b=map(int,input().split())
    cmd_list.append([a,b])

for _ in range(3):
    for i in range(K):
        s1,s2=cmd_list[i] # 변경될 자리 
        p1,p2=current_sit[s1],current_sit[s2] # 앉아있는 사람 

        #자리 내역 업데이트
        sit_list[p1].add(s2)
        sit_list[p2].add(s1)

        #자리 바꾸기 
        current_sit[s1],current_sit[s2]=p2,p1



for i in range(1,N+1):
    print(len(sit_list[i]))
    




