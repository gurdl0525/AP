from heapq import heappush, heappop


def solution(scoville, K):
    count = 0

    scoville.sort()

    while scoville[0] < K:

        if len(scoville) <= 1:
            return -1

        heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))

        count += 1

    return count
