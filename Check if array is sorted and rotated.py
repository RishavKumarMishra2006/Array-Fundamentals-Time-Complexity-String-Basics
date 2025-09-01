def is_sorted_and_rotated(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] > arr[(i+1) % n]:
            count += 1
    return count <= 1

# Example
print(is_sorted_and_rotated([3, 4, 5, 1, 2]))  # True
print(is_sorted_and_rotated([1, 2, 3]))        # True
print(is_sorted_and_rotated([3, 2, 1]))        # False
