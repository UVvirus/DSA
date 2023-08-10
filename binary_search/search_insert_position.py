

def search_insert_position(arr:[int],x: int) -> int:
    low=0
    high=len(arr)
    ans=len(arr)
    while low <= high:
        mid=(low+high)//2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1
    print(ans)
    return ans

if __name__ == "__main__":
    arr=[1,2,4,7]
    x=2
    search_insert_position(arr,x)