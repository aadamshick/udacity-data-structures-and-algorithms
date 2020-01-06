def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quicksort(input_list)

    num1 = ""
    num2 = ""

    for i, x in enumerate(input_list):

        if i % 2 == 1:
            num1 = str(x) + num1
        else:
            num2 = str(x) + num2

    return (int(num1), int(num2))

def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)

def quicksort(items):
    sort_all(items, 0, len(items) - 1)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# test 1
test_function([[5, 4, 3, 2, 1], [542, 31]])

# test 2
test_function([[1, 2, 3, 4, 5], [542, 31]])

# test 3
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
