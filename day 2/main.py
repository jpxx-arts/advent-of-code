def score_logic(enemy_chose, my_chose):
    if enemy_chose == 'A' and my_chose == 'X':
        return 3 + 1
    elif enemy_chose == 'A' and my_chose == 'Y':
        return 6 + 2
    elif enemy_chose == 'A' and my_chose == 'Z':
        return 0 + 3
    elif enemy_chose == 'B' and my_chose == 'X':
        return 0 + 1
    elif enemy_chose == 'B' and my_chose == 'Y':
        return 3 + 2
    elif enemy_chose == 'B' and my_chose == 'Z':
        return 6 + 3
    elif enemy_chose == 'C' and my_chose == 'X':
        return 6 + 1
    elif enemy_chose == 'C' and my_chose == 'Y':
        return 0 + 2
    elif enemy_chose == 'C' and my_chose == 'Z':
        return 3 + 3

def get_score(lines):
    score = 0

    for round in lines:
        score += score_logic(round[0], round[2])

    return score



with open('./day 2/input.in') as input:
    lines = input.readlines()

print(get_score(lines))