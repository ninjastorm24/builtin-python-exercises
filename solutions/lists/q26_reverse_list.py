"""
Q26: Reverse a list without using slicing.

Example:
>>> reverse_list([1, 2, 3, 4])
[4, 3, 2, 1]
"""

def reverse_list(lst: list) -> list:
    result = []
    for item in lst:
        result.insert(0, item)
    return result

if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4]))  # Expected: [4, 3, 2, 1]
