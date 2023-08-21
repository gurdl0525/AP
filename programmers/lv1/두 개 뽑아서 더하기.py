# 월간 코드 챌린지 시즌1
def solution(numbers):
    answer = list()

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])

    return list(set(answer))
