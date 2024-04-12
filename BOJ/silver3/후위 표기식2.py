# 후위 표기식 2

# input
# 5
# ABC*+DE/-
# 1
# 2
# 3
# 4
# 5

# output
# 6.20

# ----------------------------------------------------------------------------------------------------------------------


from collections import deque


def solution():
    N: int = int(input())
    postfix_notation: str = input()
    operand_value = dict()

    for v in postfix_notation:
        if v != '+' and v != '-' and v != '*' and v != '/':
            if operand_value.get(v) is None:
                operand_value[v] = float(input())

    stack = deque()

    for v in postfix_notation:
        if v == '+':
            stack.append(stack.pop() + stack.pop())
        elif v == '-':
            tmp = stack.pop()
            stack.append(stack.pop() - tmp)
        elif v == '*':
            stack.append(stack.pop() * stack.pop())
        elif v == '/':
            tmp = stack.pop()
            stack.append(stack.pop() / tmp)
        else:
            stack.append(operand_value[v])

    result = str(round(stack.popleft(), 2))

    print(result if len(result.split('.')[1]) == 2 else (result + '0'))


if __name__ == '__main__':
    solution()
