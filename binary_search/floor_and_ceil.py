
def floor(arr:[int],x:int):
    low=0
    high=len(arr)

    floor=-1

    while low <= high:
        mid=(low+high)//2

        if arr[mid] <= x: #Explanation: 7 < 5 false, so else condition will execute,the value we need to find is 5, it is less than 7
            floor=arr[mid]  # so it is going to be in left side, so we are moving the high pointer to the left
            low = mid + 1
        else:
            high = mid - 1

    print(floor)
    return floor
def ceil(arr:[int],x:int):
    low=0
    high=len(arr)
    ceil=-1


    while low <= high:
        mid=(low+high)//2

        if arr[mid] >= x:
            ceil=arr[mid]
            high=mid-1
        else:
            low=mid+1
    print(ceil)
    return ceil




if __name__ == "__main__":
    arr=[3, 4, 4, 7, 8, 10]
    x=8

    floor(arr,x)
    ceil(arr, x)