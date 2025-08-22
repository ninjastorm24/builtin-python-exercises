"""
Count the number of vowels in a string.

Examples:
>>> q02_count_vowels("example")
3
>>> q02_count_vowels("hello world")
3
>>> q02_count_vowels("xyz")
0
>>> q02_count_vowels("AEIOU")
5
>>> q02_count_vowels("Python Programming")
4
"""

def q02_count_vowels(s: str) -> int:
    count = 0
    vowels = 'aeiouAEIOU'#
    for char in s:
        if char in vowels:
            count = count+1
    return count        



    

if __name__ == "__main__":
    print("This is a placeholder for testing")
    print(q02_count_vowels("hello world"))
