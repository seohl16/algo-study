# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 연습문제 > 귤고르기
def solution(k, tangerine):
    answer = 0
    cnt_dict = dict()
    cnt_set = set()
    for i in tangerine: 
        if i not in cnt_dict.keys(): 
            cnt_dict[i] = 1
        else: 
            cnt_dict[i] += 1
    cnt_set = sorted(list(cnt_dict.values()), reverse=True)
    current_idx = 0
    while k > 0: 
        k = k - cnt_set[current_idx]
        answer += 1
        current_idx += 1
        if k > 0: 
            continue
        else: 
            break
    return answer
