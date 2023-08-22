def solution(progresses, speeds):
    count = []

    i = 0
    while True:

        progresses = [x + y for x, y in zip(progresses, speeds)]

        if progresses[i] >= 100:
            count.append(0)

            while progresses[i] >= 100:

                i += 1
                count[len(count) - 1] += 1

                if i >= len(progresses):
                    return count
