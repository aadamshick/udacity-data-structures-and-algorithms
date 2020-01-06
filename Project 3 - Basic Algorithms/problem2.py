def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    start = 0
    end = len(input_list)

    p = find_pivot(input_list, start, end)

    if number > input_list[p]:
        return -1
    elif number >= input_list[0]:
        return find_value(input_list, number, 0, p)
    else:
        return find_value(input_list, number, p+1, len(input_list))

def find_pivot(arr, beg, end):
    mid = beg + (end - beg) // 2

    if arr[mid] > arr[mid+1]:
        return mid

    if arr[beg] > arr[mid]:
        return find_pivot(arr, beg, mid-1)

    else:
        return find_pivot(arr, mid+1, end)

def find_value(arr, n, beg, end):
    mid = beg + (end - beg) // 2

    if arr[mid] == n:
        return mid

    if arr[mid] > n:
        return find_value(arr, n, beg, mid-1)

    else:
        return find_value(arr, n, mid+1, end)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# test 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

# test 2
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

# test 3
test_function([[6, 7, 8, 1, 2, 3, 4], 8])

# test 4
test_function([[6, 7, 8, 1, 2, 3, 4], 1])

# test 5
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
