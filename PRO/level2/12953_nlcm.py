# https://school.programmers.co.kr/learn/courses/30/lessons/12953
def solution(arr): 
    def gcd(a, b): 
        while b != 0: 
            a, b = b, a% b
        return a
    
    if len(arr) == 1: 
        return arr[0]
    
    g = gcd(arr[0], arr[1])
    answer = (arr[0] * arr[1]) // g
    if len(arr) > 2: 
        for i in range(2, len(arr)): 
            g = gcd(answer, arr[i])
            answer = (answer * arr[i]) // g
    
    return answer
