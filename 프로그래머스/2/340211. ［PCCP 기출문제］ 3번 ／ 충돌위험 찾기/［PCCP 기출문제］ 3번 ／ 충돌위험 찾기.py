from collections import Counter

def solution(points, routes):
    points=[[0,0]] + points
    answer = 0
    def find_position_by_second(route): # (x,y,second) 원소가 담긴 리스트를 return 
        second=0
        li=[]
        for i in range(len(route)-1):
            sx,sy=points[route[i]]
            ex,ey=points[route[i+1]]
            
            #x위치 먼저 맞춰주기 
            while sx!=ex:
                li.append((sx,sy,second))
                
                if sx<ex:
                    sx+=1
                elif sx>ex:
                    sx-=1
                
                second+=1
            
            #y위치 맞춰주기
            while sy!=ey:
                li.append((sx,sy,second))
                if sy<ey:
                    sy+=1
                elif sy > ey:
                    sy-=1
                
                second+=1
            
            
        li.append((sx,sy,second))
        return li
                
        
    
    
    positions=[]
    for route in routes:
        positions+=find_position_by_second(route)
    
    
    counter_li=Counter(positions) # 같은 원소가 있는지 확인 (x,y,second)
    
    #print(counter_li)
    for v in counter_li.values():
        if v>=2:
            answer+=1
    
    
        
    
    return answer