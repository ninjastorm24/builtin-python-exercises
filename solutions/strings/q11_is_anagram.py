"""
Check if a string is an anagram of another string.

Example:
>>> q11_is_anagram("listen", "silent")
True  # rearranged letters

>>> q11_is_anagram("triangle", "integral")
True

>>> q11_is_anagram("apple", "papel")
True

>>> q11_is_anagram("rat", "car")
False  # different letters

>>> q11_is_anagram("night", "thing")
True

>>> q11_is_anagram("Hello", "hello")
False  # case-sensitive unless handled

>>> q11_is_anagram("aabb", "bbaa")
True

>>> q11_is_anagram("aabb", "ab")
False  # lengths differ

>>> q11_is_anagram("", "")
True  # empty strings are trivially anagrams

>>> q11_is_anagram("123", "321")
True  # numbers also work as characters
"""


def q11_is_anagram(s1, s2):
    freq1 = {}
    for char in s1:
        if char in freq1:
            freq1[char] = freq1[char] + 1
        else: 
            freq1[char] = 1

    freq2 = {}
    for char in s2:
        if char in freq2:
            freq2[char] = freq2[char] + 1
        else: 
            freq2[char] = 1


    return freq1 == freq2

if __name__ == "__main__":
    print(q11_is_anagram("aabb", "ab"))
