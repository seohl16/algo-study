# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque 

def solution(maps): 
    
    que = deque()
    steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    que.append([0, 0, 1])
    # print(que)
    visited_set = set()
    
    while que: 
        cy, cx, cstep = que.popleft()
        if (cy, cx) in visited_set: 
            continue 
        if cy == (len(maps)-1) and cx == (len(maps[0])-1): 
            return cstep 
        visited_set.add((cy, cx))
        for step in steps: 
            ny, nx = cy + step[0], cx + step[1]
            if 0<= ny <= (len(maps)-1) and 0 <= nx <= (len(maps[0])-1) and maps[ny][nx] != 0:
                que.append([ny, nx, cstep+1])
        print(que)
        # print(cy, cx, cstep)
    return -1
