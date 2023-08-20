def solution(arr):
    answer = []

    n = -1

    for i in range(len(arr)):
        if n != arr[i]:
            n = arr[i]
            answer.append(n)
        else:
            continue

    return answer
