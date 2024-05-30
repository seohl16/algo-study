def solution(sequence, k):
    answer = []
    if k in sequence:
        ind= sequence.index(k)
        return [ind, ind]
    bucket_lst = [0] * len(sequence)
    st =0
    ed=1
    summ = sequence[0] + sequence[1]
    print(summ)
    final_res = [-1, len(sequence)]
    while ed < len(sequence) : 
        if summ < k : 
            ed += 1 
            if ed == len(sequence):
                break
            summ += sequence[ed]
        elif summ == k: 
            if ed-st < final_res[1] - final_res[0]:
                final_res = [st, ed]
            ed += 1 
            if ed == len(sequence):
                break
            summ += sequence[ed]
            
        
        else:
            summ -= sequence[st]
            st += 1 
            
    # print(bucket_lst
    return final_res