#You are given a sorted array which is rotated at some random pivot point.
#Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
#You are given a target value to search. If found in the array return its index, otherwise return -1.
#You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    length = len(input_list) -1
    pivot = find_pivot_using_binary_search(input_list, 0, length)

    if pivot == -1:
        return binary_search(input_list, 0, length -1 , number)

    if input_list[pivot] == number:
        return pivot

    if input_list[0] <= number:
        return binary_search(input_list, 0 , pivot-1, number)
    return binary_search(input_list, pivot+1 , length-1 , number)

def find_pivot_using_binary_search(array,start, end):
    if start > end:
        return -1
    if start == end:
        return start

    middle = (start + end)//2
    # middle < end
    if (middle < end) and array[middle] > array[middle + 1]:
        return middle

    # middle > start
    if (middle > start) and array[middle] < array[middle - 1]:
        return middle -1

    if array[start] >= array[middle]:
        return find_pivot_using_binary_search(array, start, middle -1)

    return find_pivot_using_binary_search(array, middle + 1, end)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def binary_search(array, start, end, target):
    while(start <= end):
        middle = (start + end)//2
        middle_value = array[middle]

        if target == middle_value:
            return middle

        elif target < middle_value:
            end = middle -1

        else:
            start = middle + 1
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# edge-case
#test_function([[], ])
#test_function([[], 10])
#test_function([[6, 7, 8, 1, 2, 3, 4]])

#output
#Pass
#Pass
#Pass
#Pass
#Pass
#Traceback (most recent call last):
#  File "P2-search-rotated-sorted-array.py", line 85, in <module>
#    test_function([[], ])
#  File "P2-search-rotated-sorted-array.py", line 72, in test_function
#    number = test_case[1]
#IndexError: list index out of range
