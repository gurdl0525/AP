# 2022 KAKAO TECH INTERNSHIP
from collections import deque


def solution(queue1, queue2):
    s1 = sum(queue1)

    s = s1 + sum(queue2)

    if s % 2:
        return -1

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    s = int(s / 2)

    count, max = 0, len(queue1) * 4

    while s1 != s:

        if count >= max:
            return -1

        elif s1 < s:
            n = queue2.popleft()
            queue1.append(n)
            s1 += n

        else:
            n = queue1.popleft()
            queue2.append(n)
            s1 -= n

        count += 1

    return count
