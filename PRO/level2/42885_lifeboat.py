# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 탐욕법(greedy) > 구명보트
def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    st, ed = 0, len(people) - 1
    while st <= ed:
        answer += 1
        if people[st] + people[ed] <= limit: 
            st += 1
            ed -= 1
        else: 
            st += 1
        # print(st, ed)
        
    return answer
