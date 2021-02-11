#In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    length = len(ints)
    if length == 0:
        return (None,None)

    min = ints[0]
    max = ints[1]

    if min > max:
        max,min = min, max

    for i in range(2,length):
        if ints[i] > max:
            max = ints[i]
        elif ints[i] < min:
            min = ints[i]
    return (min,max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
