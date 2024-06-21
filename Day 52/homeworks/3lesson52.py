# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python


def filter_list(l):
    filtered_list = []
    for item in l:
        if type(item) != str:
            filtered_list.append(item)
    return filtered_list

        