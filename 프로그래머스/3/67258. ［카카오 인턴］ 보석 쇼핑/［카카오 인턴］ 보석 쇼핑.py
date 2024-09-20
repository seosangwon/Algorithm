from collections import defaultdict

def solution(gems):
    INF = int(1e9)
    answer = [0, INF]
    
    left, right = 0, 0
    N = len(gems)
    gem_set = set(gems)
    gem_total_cnt = len(gem_set)  # 보석의 총 종류 수
    gems_dict = defaultdict(int)
    gems_dict[gems[0]] = 1  # 첫 번째 보석 추가

    while right < N:
        if len(gems_dict) == gem_total_cnt:
            # 현재 구간이 모든 보석을 포함하면 답 갱신
            if right - left < answer[1] - answer[0]:
                answer = [left + 1, right + 1]  # 인덱스는 1부터 시작하므로 +1
            # left 포인터 이동 및 gems_dict 갱신
            gems_dict[gems[left]] -= 1
            if gems_dict[gems[left]] == 0:
                del gems_dict[gems[left]]
            left += 1
        else:
            right += 1
            if right == N:
                break
            # right 포인터가 가리키는 보석 추가
            gems_dict[gems[right]] += 1

    return answer