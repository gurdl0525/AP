# 송아지 찾기(BFS: 상태트리탐색)

# input
# 5 14

# output
# 3

from collections import deque


def solution():
    S, E = map(int, input().split())

    print(bfs(S, E))


def bfs(_S: int, _E: int) -> int:
    queue, visited = deque(), []
    queue.append([_S, 0])

    while queue:
        stmp = queue.popleft()
        s1, s2 = stmp[0], stmp[1]

        if s1 == _E:
            return s2

        plus_one, plus_five, minus_one = s1 + 1, s1 + 5, s1 - 1

        if plus_one <= 10000 and plus_one <= _E and plus_one not in visited:
            queue.append([plus_one, s2 + 1])
            visited.append(plus_one)

        if plus_five <= 10000 and plus_five <= _E and plus_five not in visited:
            queue.append([plus_five, s2 + 1])
            visited.append(plus_five)

        if 1 <= minus_one and _E <= minus_one and minus_one not in visited:
            queue.append([minus_one, s2 + 1])
            visited.append(minus_one)


if __name__ == '__main__':
    solution()
