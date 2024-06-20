# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 스택/큐 > 다리를 지나는 트럭
from collections import deque 

def solution(bridge_length, weight, truck_weights): 
    
    bridge = deque([0] * (bridge_length))
    truck_weights = deque(truck_weights)
    
    time = 0
    currentWeight = 0
    while len(truck_weights) > 0: 
        time += 1
        
        currentWeight = currentWeight - bridge.popleft()
        if currentWeight + truck_weights[0] <= weight: 
            # you can putit 
            tmp = truck_weights.popleft()
            bridge.append(tmp)
            currentWeight += tmp
        else: 
            bridge.append(0)
            
        if len(truck_weights) == 0: 
            return time + bridge_length
