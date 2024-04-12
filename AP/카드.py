# 카드

from collections import deque


def solution():

    N = int(input())

    queue = deque(range(1, N + 1))

    queue.popleft()

    while queue:
        queue.append(queue.popleft())
        queue.popleft()

    print(queue.popleft())


if __name__ == '__main__':
    solution()
