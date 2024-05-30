def solution(n, s):
    if n > s: 
        return [-1]
    st_val = s // n
    answer = [st_val] * n
    for i in range(s % n):
        answer[len(answer)-i-1] += 1
    
    return answer

