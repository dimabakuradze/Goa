def num(hello, baro, zd):
    for i in range(len(hello)):
        if hello[i] == baro:
            hello[i] = zd
    return hello


original_list = [10, 11, 10, 11]
target_number = 10
replacement_number = 20
new_list = num(original_list, target_number, replacement_number)
print(new_list) 
