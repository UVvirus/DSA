"""
Lower bound means the lowest index of that value
intha value(X) or intha value of perusa irukra first value entha index la irukudho
adha kanda pudikanum

Ex:- case 1: if we have [1,2,2,2,3,4] we need to find 2(x=2) then its lower bound could index 1,
even though there are multiple 2's we need to get the lowest index

    case 2: If the number is present in betwwen, then we need to find the next largest number.
    Ex:if we have [1,2,4,5,6] and we need to find x=3, then its lower bound could be 4,because
    3 is present inbetween 2 & 4.

    case 3: if the number is not present in the array then print the length of the array,
    because it is the least number.

"""

"""
Algo:
 We used Binary search here. 
 1) First we need to set low and high to find mid.
 2) mid can be found using low + high // 2
 3) if the value of mid is greater than or equal to X then that is probably our answer,so
 save it in "ans" variable.
 (i.e.,) if the value is 6 but our mid value is 8, then it is going to be insisde this limit
 so we can limit our search space by high = mid - 1
 
 if the nearest value has been matched, save it on answer variable, bcoz that could be the answer.
 
 4) if the value is 7 but our mid value is 5, then the value is going to be in left side,so set
 low=mid+1
 
 5) if no value is matched then return the length of the array

"""

def method1(arr: [int], x: int) -> int:

    """

    :param arr: is an integer array
    :param x: is the value we need to find from the given array
    :return: index
    """
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1

        elif arr[mid] < x:
            low = mid + 1

    return ans


if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    x = 8
    method1(arr, x)
