# https://school.programmers.co.kr/learn/courses/30/lessons/12941
# 최솟값 만들기 
def solution(A,B):
    answer = 0

    A = sorted(A)
    B = sorted(B, reverse=True)
    #  sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
    # good solution
    
    summ = 0
    for i in range(len(A)): 
        summ += A[i] * B[i]

    return summ
