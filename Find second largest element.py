def second_largest(arr):
    unique = list(set(arr))  # remove duplicates
    if len(unique) < 2:
        return -1
    unique.sort()
    return unique[-2]

# Example
print(second_largest([12, 35, 1, 10, 34, 1]))  # 34
