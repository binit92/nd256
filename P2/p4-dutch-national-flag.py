#Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

#Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    merge_sort(input_list)
    return input_list


def merge_sort(arr):
    length = len(arr)
    large_reversal_count = 0
    if length > 1:

        mid = length // 2

        LEFT_ARR = arr[:mid]
        length_LEFT_ARR = len(LEFT_ARR)

        RIGHT_ARR = arr[mid:]
        length_RIGHT_ARR = len(RIGHT_ARR)

        # splitting starts from these recursive calls
        merge_sort(LEFT_ARR)
        merge_sort(RIGHT_ARR)

        # merging starts from here
        i = j = k = 0
        while i < length_LEFT_ARR and j < length_RIGHT_ARR:
            if LEFT_ARR[i] < RIGHT_ARR[j]:
                arr[k] = LEFT_ARR[i]
                i+=1
            else:
                arr[k] = RIGHT_ARR[j]
                j+=1
            k+=1

        # merge if any remaining items in left
        while i <length_LEFT_ARR:
            arr[k] = LEFT_ARR[i]
            i+=1
            k+=1

        # merge if any remaining items in right
        while j<length_RIGHT_ARR:
            arr[k]= RIGHT_ARR[j]
            j+=1
            k+=1



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
