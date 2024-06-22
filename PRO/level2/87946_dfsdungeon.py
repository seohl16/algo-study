# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 완전탐색 > 피로도 

def dfs(k, dungeons, visited, step): 
    maxx = step 
    if k < 0: 
        return maxx
    for i in range(len(dungeons)): 
        if visited[i] == 0 and k - dungeons[i][0] >= 0: 
            visited[i] = 1
            result = dfs(k - dungeons[i][1], dungeons, visited, step+1)
            visited[i] = 0
            if result > maxx: 
                maxx = result
    return maxx


def solution(k, dungeons): 
    
    visited = [0] * len(dungeons)
    step = 0
    maxx = dfs(k, dungeons, visited, step)
    
    return maxx
