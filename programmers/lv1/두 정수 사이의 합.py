def solution(a, b):
    min, max = int(), int()

    if a > b:
        min = b
        max = a
    else:
        min = a
        max = b

    answer = 0

    while True:
        answer += min
        min += 1
        if min > max:
            break

    return answer
