# 2022 KAKAO BLIND RECRUITMENT
def solution(id_list, report, k):
    people = {v: [] for v in id_list}

    for r in report:
        r = r.split(' ')
        if r[0] not in people[r[1]]:
            people[r[1]].append(r[0])

    result = {v: 0 for v in id_list}
    for p in people.values():
        if len(p) >= k:
            for person in p:
                result[person] += 1

    return [v for v in result.values()]
