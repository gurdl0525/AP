# 가장 큰 수

# 선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다.
# 여러분이 현수를 도와주세요. (단 숫자의 순서는 유지해야 합니다)
# 만약 5276823이 주어지고 3개의 자릿수를 제거 한다면 7823이 가장 큰 숫자가 됩니다.

# input
# 5276823 3

# output
# 7823

# ----------------------------------------------------------------------------------------------------------------------

from collections import deque


def solution():
    N, K = input().split()

    N = [int(num) for num in N]
    K = int(K)

    stack = []

    for i in N:
        while len(stack) != 0 and i > stack[-1] and K > 0:
            stack.pop()
            K -= 1
        stack.append(i)

    print(* stack[: -K if K != 0 else len(stack)], sep='')


if __name__ == '__main__':
    solution()
