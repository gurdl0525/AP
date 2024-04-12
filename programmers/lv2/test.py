# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
import numpy as np


def solution(rows, columns, queries):
    lists = np.array(range(1, rows * columns + 1)).reshape(rows, columns)
    print(lists)

    result, middle = [], []

    for query in queries:
        x1, y1 = query[0] - 1, query[1] - 1
        x2, y2 = query[2] - 1, query[3] - 1
        middle.append(lists[y1][x1])

        i, j = y1 + 1, x1
        while i != y1 or j != x1:
            i

        result.append(min(middle))
        middle.clear()

    return result
