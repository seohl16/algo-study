# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 2017 팁스타운 > 예상 대진표
def solution(n,a,b):
    answer = 0
    while True: 
        answer += 1
        ret = (a-1) // 2 
        ret2 = (b-1) // 2
        # print(ret, ret2)
        if ret == ret2 : 
            break
        a = (a-1) // 2 + 1
        b = (b-1) // 2 + 1

    return answer
