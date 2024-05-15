def num (xello, baro):
    count = 0
    for element in xello:
        if element == baro:
            count += 1
    return count


original_list = [12, 13, 14, 12, 14, 100]
target_number = 12
zd = num(original_list, target_number)
print(zd) 
