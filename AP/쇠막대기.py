# 쇠막대기

# input
# ()(((()())(())()))(())

# output
# 17


def solution():
    stin = str(input())

    stack = []

    count = 0

    for i, v in enumerate(stin):
        if v == '(':
            stack.append(v)
        else:
            stack.pop()
            if stin[i - 1] == '(':
                count += len(stack)
            else:
                count += 1

    print(count)


if __name__ == '__main__':
    solution()
