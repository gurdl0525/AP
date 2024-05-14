# 사과나무(BFS)

# input
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# output
# 379

from collections import deque


def solution():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    middle = int(N / 2)

    print(bfs(middle, A, N))


def bfs(_middle: int, _A: list, _N: int) -> int:
    queue, _sum = deque(), 0
    queue.append([[0, 0], 0])

    visited = [[0, 0]]

    while queue:
        tmp = queue.popleft()
        i1, i2 = tmp[0][0], tmp[0][1]
        m1, m2 = _middle + i1, _middle + i2

        _sum += _A[m1][m2]

        arr1, arr2, arr3, arr4 = [i1, i2 + 1], [i1, i2 - 1], [i1 + 1, i2], [i1 - 1, i2]

        if tmp[1] != _middle and arr1 not in visited:
            queue.append([arr1, tmp[1] + 1])
            visited.append(arr1)

        if tmp[1] != _middle and arr2 not in visited:
            queue.append([arr2, tmp[1] + 1])
            visited.append(arr2)

        if tmp[1] != _middle and arr3 not in visited:
            queue.append([arr3, tmp[1] + 1])
            visited.append(arr3)

        if tmp[1] != _middle and arr4 not in visited:
            queue.append([arr4, tmp[1] + 1])
            visited.append(arr4)

    return _sum


if __name__ == '__main__':
    solution()
