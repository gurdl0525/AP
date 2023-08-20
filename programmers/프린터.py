def solution(priorities, location):
    count = 1

    while True:

        if max(priorities) <= priorities[0]:

            if location == 0:
                location = len(priorities) - 1
                return count

            else:
                location -= 1
                priorities.pop(0)

            count += 1

        else:
            priorities.append(priorities.pop(0))
            location = len(priorities) - 1 if location == 0 else location - 1
