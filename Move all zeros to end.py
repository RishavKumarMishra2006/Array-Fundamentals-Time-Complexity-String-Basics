def move_zeros(arr):
    non_zeros = [x for x in arr if x != 0]
    zeros = [0] * (len(arr) - len(non_zeros))
    return non_zeros + zeros

# Example
print(move_zeros([0, 1, 9, 8, 4, 0, 0, 2, 7, 0]))  # [1, 9, 8, 4, 2, 7, 0, 0, 0, 0]
