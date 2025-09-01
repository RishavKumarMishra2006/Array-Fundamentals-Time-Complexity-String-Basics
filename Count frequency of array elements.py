from collections import Counter

def frequency_count(arr):
    return dict(Counter(arr))

# Example
print(frequency_count([2, 3, 2, 3, 5]))  
# {2: 2, 3: 2, 5: 1}
