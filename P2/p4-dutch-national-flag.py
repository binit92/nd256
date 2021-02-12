#Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

#Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    print(input_list)
    arr = input_list
    start = 0
    next = 0
    end = len(arr) -1
    while start <=end:
        if arr[start] == 0:
            arr[start] = arr[next]
            arr[next] = 0
            next+=1
            start+=1
        elif arr[start] == 2:
            arr[start] = arr[end]
            arr[end] = 2
            end -= 1
        else:
            start += 1
    return arr



def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")



test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# egecase
test_function([])
test_function([0, 1, 2])

#output
#[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
#[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
#Pass
#[2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#Pass
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
#Pass
#[]
#[]
#Pass
#[0, 1, 2]
#[0, 1, 2]
#Pass
