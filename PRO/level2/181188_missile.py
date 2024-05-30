def solution(targets):
    answer = 0
    sorted_targets = sorted(targets, key=lambda x: x[1])
    #print(sorted_targets)
    
    shoots = -1
    for a, b in sorted_targets: 
        #print(a, b)
        if shoots < a: 
            shoots = b - 0.5 
            answer += 1
    return answer
