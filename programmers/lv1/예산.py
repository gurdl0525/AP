# Summer/Winter Coding(~2018)
def solution(d, budget):
    count = 0

    while d:

        budget -= d.pop(d.index(min(d)))

        if budget >= 0:
            count += 1

        if budget <= 0:
            break

    return count
