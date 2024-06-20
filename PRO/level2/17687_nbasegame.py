# https://school.programmers.co.kr/learn/courses/30/lessons/17687
# 2018 KAKAO BLIND RECRUITMENT [3차] n진수 게임

def convert(i, n): 
    numstring = '0123456789ABCDEF'
    q, r = divmod(i, n)
    
    if q == 0: 
        return numstring[r]
    else: 
        return convert(q, n) + numstring[r]

def solution(n, t, m, p): 
    answer = ''
    test = ''
    
    for i in range(m*t): 
        test += str(convert(i, n))
    
    i = 0
    while i < t: 
        answer += test[m * i + p - 1]
        i += 1
        
    return answer
