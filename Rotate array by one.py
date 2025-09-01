def rotate_by_one(arr):
    if len(arr) == 0:
        return arr
    last = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last
    return arr

# Example
print(rotate_by_one([1, 2, 3, 4, 5]))  # [5, 1, 2, 3, 4]
