import heapq

def solution(targets):
    answer = 0
    targets.sort(key=lambda x: (x[1] , x[0]))
    s = e = 0
    #print(targets)
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]
           # print(target[0])


    return answer