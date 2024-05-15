"""Write a function which calculates the average of the numbers in a given list.
"""


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


numbers_list = [1, 2, 3,]
print("Average:", calculate_average(numbers_list))  
