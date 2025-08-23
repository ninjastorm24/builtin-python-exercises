"""
Find the most frequent character in a string.

Example:
>>> q10_most_frequent_char("example")
"e"   # 'e' appears 2 times, more than others

>>> q10_most_frequent_char("hello world")
"l"   # 'l' appears 3 times

>>> q10_most_frequent_char("mississippi")
"i"   # 'i' appears 4 times, tied with 's' (both appear 4 times) → return either

>>> q10_most_frequent_char("aabbbcccc")
"c"   # 'c' appears 4 times

>>> q10_most_frequent_char("xyz")
"x"   # all occur once → return the first one

>>> q10_most_frequent_char("")
""    # empty string → return empty (edge case)

>>> q10_most_frequent_char("112233")
"1"   # numbers also count as characters
"""


def q10_most_frequent_char(s):
    if s == "":
        return ""
    
    freq = {}
    
    for char in s:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1

    max_count = 0
    freq_char = ""
    for char in s:
        if freq[char]  > max_count:
            max_count = freq[char]
            freq_char = char
    return freq_char 







if __name__ == "__main__":
    print(q10_most_frequent_char("aabbbcccc"))
