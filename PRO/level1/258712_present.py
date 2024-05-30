def solution(friends, gifts):
    answer = 0
    present_box = []
    present_idx = {}
    for idx, f in enumerate(friends): 
        present_box.append([0] * len(friends))
        present_idx[f] = idx
    present_etf = [0] * len(friends)
    for idx, g in enumerate(gifts):
        fo_, to_ = g.split(' ')
        (present_box[present_idx[fo_]][present_idx[to_]]) += 1
        present_etf[present_idx[fo_]] += 1
        present_etf[present_idx[to_]] -= 1
    print(present_etf)
    conclud_pre = []
    for i in range(len(present_box)):
        # i means the idx of a person 
        present = 0
        for j in range(len(present_box[i])):
            if i == j : 
                continue 
            if present_box[i][j] > present_box[j][i] : # if muzi gave more 
                present += 1
            elif present_box[i][j] == present_box[j][i] : # if same 
                if present_etf[i] > present_etf[j]: 
                    present += 1
        conclud_pre.append(present)
    print(conclud_pre)
    answer = max(conclud_pre)
    return answer