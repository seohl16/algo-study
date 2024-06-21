# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 스택/큐 > 프로세스
from collections import deque 

def solution(priorities, location):
    answer = 0
    prior_que = deque(priorities)
    idx_que = deque([i for i in range(len(priorities))])
    cnt = 1
    
    while (len(prior_que) > 0): 
        item = prior_que.popleft()
        idx = idx_que.popleft()
        if prior_que and max(prior_que) > item: 
            prior_que.append(item)
            idx_que.append(idx)
        else: 
            if idx == location: 
                return cnt 
            cnt += 1
        # print(idx, prior_que)
    return answer

""" 
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
"""
