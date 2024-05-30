def solution(number, k): 
    answer = []
    
    for num in number: 
        while k > 0 and answer and answer[-1] < num: 
            answer.pop()
            k -= 1
        answer.append(num)
    return ''.join(answer[:len(answer)-k])
    
    
# def solution(number, k):
#     answer = ''
#     original_len = len(number) - k
#     number_lst = number
#     break_while = 0
#     while k != 0: 
#         for ind in range(len(number_lst)): 
#             if number_lst[ind] >= number_lst[ind+1]: 
#                 continue
#             elif number_lst[ind] < number_lst[ind+1]:
#                 number_lst = number_lst[:ind] + number_lst[ind+1:]
#                 k -= 1
#                 break
#             else:
#                 break_while = 1
#         if break_while: 
#             break
            
#     answer = number_lst
#     if k > 0: 
#         answer = answer[:original_len]
    
#     return answer
