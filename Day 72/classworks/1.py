def sort_array(source_array):
    odd_numbers = sorted(num for num in source_array if num % 2 != 0)
    odd_iter = iter(odd_numbers)
    sorted_array = [next(odd_iter) if num % 2 != 0 else num for num in source]
