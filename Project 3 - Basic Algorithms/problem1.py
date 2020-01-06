def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    elif number < 3:
        return 1
    else:
        return sqrt_recurse(number, 0, number)

def sqrt_recurse(n, min, max):
    m = min + ((max - min) // 2)
    sqr = m * m

    if (m * m <= n < (m+1) * (m+1)):
        return m

    elif m * m > n:
        return sqrt_recurse(n, min, m)

    elif m * m < n:
        return sqrt_recurse(n, m, max)

# test 1
print ("Pass" if  (3 == sqrt(9)) else "Fail")

# test 2
print ("Pass" if  (0 == sqrt(0)) else "Fail")

# test 3
print ("Pass" if  (4 == sqrt(16)) else "Fail")

# test 4
print ("Pass" if  (1 == sqrt(1)) else "Fail")

# test 5
print ("Pass" if  (5 == sqrt(27)) else "Fail")
