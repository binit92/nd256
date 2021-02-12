# find the square root of an integer without using any python library ..
# using binary search to find the square Root

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if (number == 0) or (number == 1):
        return number

    if number < 0:
        return sqrt(number * (-1))

    first = 1
    last = number
    output = 1
    while(first <= last):
        # double // for integer number
        middle = (first + last)//2


        # only stands true for 4?
        if (middle * middle) == number:
            return middle

        if (middle * middle) < number:
            first = middle + 1
            output = middle

        else:
            last = middle -1
            #print(last)

    return output

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

#test-cases
print(sqrt(-64))
print(sqrt(625))
print(sqrt(-1))

#output
#Pass
#Pass
#Pass
#Pass
#Pass
#8
#25
#1
