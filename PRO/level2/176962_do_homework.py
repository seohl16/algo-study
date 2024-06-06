# 한번 틀린 문제 

def solution(plans): 
    
    for i in range(len(plans)):
        ih, im = map(int, plans[i][1].split(":"))
        timeinminute = ih * 60 + im 
        plans[i][1] = timeinminute
        plans[i][2] = int(plans[i][2])
    plans = sorted(plans, key=lambda x: x[1])
    
    stack = []
    answer = []
    
    for i in range(len(plans)): 
        if i == len(plans)-1: 
            stack.append(plans[i])
            break
        
        na, st, play = plans[i]
        nna, nst, nplay = plans[i+1]
        if st + play <= nst: 
            answer.append(na)
            tmp_time = nst - (st + play)
            while tmp_time != 0 and stack:
                tna, tst, tplay = stack.pop()
                if tmp_time - tplay >= 0:
                    answer.append(tna)
                    tmp_time -= tplay 
                else: 
                    stack.append([tna, tst, tplay - tmp_time])
                    tmp_time = 0 # 이걸 잊었었음
        else: 
            stack.append([na, st, play - (nst-st)])
            
    
    while (stack): 
        na, st, play = stack.pop()
        answer.append(na)
                    
            
    return answer
