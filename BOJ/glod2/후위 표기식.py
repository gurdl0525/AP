# 후위 표기식

# input
# A*(B+C)

# output
# ABC+*

# ----------------------------------------------------------------------------------------------------------------------


def solution():
    postfix_notation = input()
    stack = []

    for v in postfix_notation:
        if v == '(':
            stack.append(v)
        elif v == ')':
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()

        elif v == '*' or v == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                print(stack.pop(), end='')
            stack.append(v)

        elif v == '+' or v == '-':
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(v)

        else:
            print(v, end='')

    while stack:
        print(stack.pop(), end='')


if __name__ == '__main__':
    solution()
