def find_second_smallest(my_list):
    sorted_data = sorted(my_list)
    if len(sorted_data) > 1:
        return sorted_data[1]
    return None

print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest([3, 5]))
print(find_second_smallest([2]))