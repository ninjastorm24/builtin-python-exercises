"""
Remove all vowels from a string.

Example:
>>> q09_remove_vowels("example")
"xmpl"

>>> q09_remove_vowels("hello world")
"hll wrld"

>>> q09_remove_vowels("AEIOU")
""  # all vowels removed, empty string

>>> q09_remove_vowels("Python Programming")
"Pythn Prgrmmng"

>>> q09_remove_vowels("xyz")
"xyz"  # no vowels, stays the same

>>> q09_remove_vowels("")
""  # empty input stays empty

>>> q09_remove_vowels("aEiOu")
""  # mixed-case vowels, all removed

>>> q09_remove_vowels("Data Science")
"Dt Scnc"
"""


def q09_remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join([char for char in s if char not in vowels ])



if __name__ == "__main__":
    print(q09_remove_vowels("aEiOu"))
