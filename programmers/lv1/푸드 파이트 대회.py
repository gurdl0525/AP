def solution(food):
    food = food[1:]

    for i in range(len(food)):
        food[i] = int(food[i] / 2)

    answer = ''

    for i in range(len(food)):
        for _ in range(food[i]):
            answer += str(i + 1)

    list1 = reversed(answer)

    answer += '0'

    for n in list(list1):
        answer += str(n)

    return answer
