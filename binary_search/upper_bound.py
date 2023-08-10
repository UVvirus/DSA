"""
upper bound means
intha value(X) oda periya value irukra first index edhunu find panrathu
Refer lower bound if you dont have clarity
"""

def upper_bound(arr: [int], x: int) -> int:
    low=0
    high=len(arr)

    ans=len(arr)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans=mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)
    return ans



if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7]
    x=4
    upper_bound(arr,x)