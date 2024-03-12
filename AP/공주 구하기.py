# 공주 구하기(큐 자료구조로 해결)

from collections import deque


def solution():

    N, K = map(int, input().split())

    queue = deque(range(1, N + 1))

    count = 1
    while len(queue) != 1:
        num = queue.popleft()
        if count == K:
            count = 1
        else:
            count += 1
            queue.append(num)

    print(queue.pop())