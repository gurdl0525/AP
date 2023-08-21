# 2022 KAKAO TECH INTERNSHIP
def solution(survey, choices):
    answer = ''

    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for ci in range(len(survey)):

        if choices[ci] > 4:

            personality[survey[ci][1]] += choices[ci] - 4

        elif choices[ci] < 4:

            personality[survey[ci][0]] += 4 - choices[ci]

    answer += 'R' if personality['T'] <= personality['R'] else 'T'

    answer += 'C' if personality['F'] <= personality['C'] else 'F'

    answer += 'J' if personality['M'] <= personality['J'] else 'M'

    answer += 'A' if personality['N'] <= personality['A'] else 'N'

    return answer
