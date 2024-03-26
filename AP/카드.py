# 카드

from collections import deque


def solution():

    N = int(input())

    queue = deque(range(1, N + 1))

    while True:
        queue.popleft()
        if len(queue) == 1:
            break
        queue.append(queue.popleft())

    print(queue.popleft())


if __name__ == '__main__':
    solution()
