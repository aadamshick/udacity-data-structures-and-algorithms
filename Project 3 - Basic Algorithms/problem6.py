def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = ints[0]
    max = ints[0]

    for x in ints:
        if x < min:
            min = x
        if x > max:
            max = x

    return (min, max)

import random

# test 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# test 2
l = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")

# test 3
l = [i for i in range(-10, 15)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((-10, 14) == get_min_max(l)) else "Fail")
