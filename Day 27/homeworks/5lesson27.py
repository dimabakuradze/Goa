# Highest and Lowest


def num(numbers):
    num_list = [int(num) for num in numbers.split()]
    highest = max(num_list)
    lowest = min(num_list)
    return f"{highest} {lowest}"
print(num("1 2 3 4 5")) 
