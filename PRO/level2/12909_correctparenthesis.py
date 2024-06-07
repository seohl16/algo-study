#  https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    
    stack = []
    for i in range(len(s)): 
        if s[i] == '(': 
            stack.append(s[i])
        elif s[i] == ')':
            if stack and stack[-1] == '(': 
                stack.pop()
            else: 
                return False
    # if stack: 
    #     return False # old solution
    # return True
    return len(stack) == 0 # good!
