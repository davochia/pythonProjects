def search_number(nums, number_to_find):
    count = 0
    x = range(nums)
    left = 0
    right = len(x) - 1

    while left <= right:
        count += 1
        middle = (left + right) // 2
        is_number = x[middle]

        if number_to_find == is_number:
            print("Iterations: ", count)
            return middle
        elif number_to_find < is_number:
            right = middle - 1
        else:
            left = middle + 1
    return - 1


print(search_number(700, 301))
 