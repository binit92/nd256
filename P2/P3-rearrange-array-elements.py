#Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

#for e.g. [1, 2, 3, 4, 5]

#The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    length = len(input_list)
    if length == 0:
        return 0, 0

    print(input_list)
    merge_sort(input_list)
    sorted_list = input_list
    #sorted_list = sorted(input_list)
    print(sorted_list)
    even = 0
    odd = 0

    max_sum = [0,0]
    for e, i in enumerate(range(0,length,2)):
        if i == length -1 and length%2 == 1:
             max_sum[0] += sorted_list[i] * 10 ** e
        else:
            max_sum[1] += sorted_list[i] * 10 ** e
            max_sum[0] += sorted_list[i+1] * 10 ** e

    print(max_sum)
    return max_sum


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
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
