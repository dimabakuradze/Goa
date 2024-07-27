# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python


def row_weights(array):
    team_1_weight = 0
    team_2_weight = 0
    for i in range(len(array)):
        if i % 2 == 0:
            team_1_weight += array[i]
        else:
            team_2_weight += array[i]
    return (team_1_weight, team_2_weight)