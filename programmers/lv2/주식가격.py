def solution(prices):
    count = []

    for i, p in enumerate(prices):
        count.append(0)
        j = i + 1
        while j < len(prices):

            if p > prices[j]:
                count[i] += 1
                break

            else:
                count[i] += 1
                j += 1

    return count
