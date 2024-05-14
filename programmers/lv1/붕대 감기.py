def solution(bandage, health: int, attacks):
    max_health = health

    for i, v in enumerate(attacks):
        t = v[0] - 1

        if i != 0:
            t -= attacks[i - 1][0]

        health += (bandage[2] * int(t / bandage[0])) + (bandage[1] * t)
        if health > max_health:
            health = max_health

        health -= v[1]

        if health <= 0:
            return -1

    return health


if __name__ == '__main__':
    print(solution([2, 1, 1], 8, [[1, 7], [5, 2]]))


# | time | health | success | attack |
# | 0    | 8      | 0       | X      |
# | 1    | 1(-7)  | 0       | O      |
# | 2    | 2(+1)  | 1       | X      |
# | 3    | 4(+2)  | 2->0    | X      |
# | 4    | 5(+1)  | 1       | X      |
# | 5    | 3(-2)  | 0       | O      |

