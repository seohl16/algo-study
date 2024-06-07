def solution(s):
    answer = ''
    s_lst = list(map(int, s.split(" ")))
    answer = f'{min(s_lst)} {max(s_lst)}'
    return answer
