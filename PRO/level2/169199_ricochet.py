# once 

def solution(board):
    answer = 0
    final_answer = []
    # bfs 
    visited_lst = []
    r_y, r_x = 0, 0
    for i in range(len(board)):
        visited_lst.append([])
        for j in range(len(board[0])):
            # visited_lst[i].append(0)
            if board[i][j] == 'R':
                visited_lst[i].append('R')
                r_y, r_x = i, j
            elif board[i][j] == 'D': 
                visited_lst[i].append('D')
            elif board[i][j] == 'G':
                visited_lst[i].append('G')
            else:
                visited_lst[i].append('0')
    # print(visited_lst)
    queue = [(r_y, r_x, 0)]
    max_y = len(board)
    max_x = len(board[0])
    cnt = 0
    while queue:
        c_y, c_x, step_ = queue.pop(0)
        # print(c_y, c_x)
        # to right 
        tmp_list = []
        for i in range(c_x, max_x):
            # if board max wall 
            if (i+1 != max_x and board[c_y][i+1] == 'D'): 
                tmp_list.append((c_y, i))
                break
            elif i == max_x -1: 
                tmp_list.append((c_y, i))
        # to left 
        for i in range(c_x, -1, -1): 
            if (i-1 != -1 and board[c_y][i-1] == 'D'):
                tmp_list.append((c_y, i))
                break
            elif i == 0:
                tmp_list.append((c_y, 0))
        # to up 
        for j in range(c_y, max_y): 
            # if board max wall 
            if (j+1 != max_y and board[j+1][c_x] == 'D'): 
                tmp_list.append((j, c_x))
                break
            elif j == max_y -1: 
                tmp_list.append((j, c_x))
        # to down
        for j in range(c_y, -1, -1): 
            # if board max wall 
            if (j-1 != -1 and board[j-1][c_x] == 'D'): 
                tmp_list.append((j, c_x))
                break
            elif j == 0: 
                tmp_list.append((j, c_x))
        # if c_x == 2: 
            # print('visited_lst', visited_lst)
        for y, x in tmp_list: 
            # print(y, x, visited_lst[y][x])
            if visited_lst[y][x] == 'R': 
                continue
            elif visited_lst[y][x] == 'D':
                continue 
            elif visited_lst[y][x] == 'G':
                final_answer.append((y, x, step_+1))
                return step_+1
                break
            elif visited_lst[y][x] == '1':
                continue
            elif visited_lst[y][x] == '0':
                queue.append((y, x, step_ +1))
                visited_lst[y][x] = '1'
        # print(queue)
        if final_answer: 
            break
        cnt += 1
        # if cnt == 2: 
        #     break
    # print(queue)
    if len(queue) == 0:
        return -1
    
    return answer
