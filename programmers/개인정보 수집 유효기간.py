# 2023 KAKAO BLIND RECRUITMENT
def solution(today, terms, privacies):
    answer = []

    toYear, toMinth, toDay = list(map(int, today.split('.')))

    terms = {t.split(' ')[0]: int(t.split(' ')[1]) for t in terms}

    for i, p in enumerate(privacies):

        pList = p.split(' ')

        pYear, pMonth, pDay = list(map(int, pList[0].split('.')))

        pMonth += terms[pList[1]]

        while pMonth > 12:
            pYear += 1
            pMonth -= 12

        if pYear < toYear:
            answer.append(i + 1)

        elif pYear == toYear:

            if pMonth < toMinth:
                answer.append(i + 1)

            elif pMonth == toMinth:

                if pDay <= toDay:
                    answer.append(i + 1)

    return answer
