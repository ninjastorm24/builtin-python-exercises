"""
Reverse a string without using slicing.

Example:
>>> q01_reverse_string("example")
"""

def q01_reverse_string(s):
    reverse_str = ""
    for char in s:
        reverse_str = char + reverse_str
    return reverse_str

if __name__ == "__main__":
    print(q01_reverse_string("example"))  # elpmaxe
    print(q01_reverse_string("hello"))    # olleh
