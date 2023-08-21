# 월간 코드 챌린지 시즌3
def solution(numbers):
    sum = 0

    for num in range(10):

        if num not in numbers:
            sum += num

    return sum