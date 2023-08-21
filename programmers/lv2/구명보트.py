def solution(people, limit):
    people.sort()

    count = 0

    l = 0
    r = len(people) - 1

    while l <= r:
        if limit >= people[l] + people[r]:
            l += 1
        count += 1
        r -= 1

    return count
