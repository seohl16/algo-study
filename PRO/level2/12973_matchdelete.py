# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 2017 팁스타운 > 짝지어 제거하기
from collections import deque 

def solution(s):
    answer = -1

    sta = deque()
    for al in s: 
        if len(sta) == 0: 
            sta.append(al)
            continue
        if sta[-1] == al: 
            sta.pop()
        else: 
            sta.append(al)
        # print(list(sta))
        
    return int(len(sta) == 0)
