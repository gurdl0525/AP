def solution(board, moves):
    stack = [0]
    count = 0
    for move in moves:

        for i in range(len(board)):

            if board[i][move - 1] != 0:

                if stack[-1] == board[i][move - 1]:

                    stack = stack[:-1:]
                    count += 2

                else:
                    stack.append(board[i][move - 1])

                board[i][move - 1] = 0

                break

    return count
