"""
Check if a string is a palindrome (reads the same backward).

Examples:
>>> q03_is_palindrome("madam")
True
>>> q03_is_palindrome("racecar")
True
>>> q03_is_palindrome("hello")
False
>>> q03_is_palindrome("A man a plan a canal Panama")
True   # if we ignore spaces and casing
>>> q03_is_palindrome("No lemon, no melon")
True   # if we ignore spaces, punctuation, and casing
>>> q03_is_palindrome("Python")
False
>>> q03_is_palindrome("")
True   # empty string is considered a palindrome
>>> q03_is_palindrome("a")
True   # single character is always a palindrome
"""


def q03_is_palindrome(s:str)->bool:
    reversed_str = ""
    for char in s:
        reversed_str =  char + reversed_str
    return reversed_str == s
    


    

if __name__ == "__main__":
    # Palindromes
    print(q03_is_palindrome("madam"))           # True
    print(q03_is_palindrome("racecar"))         # True
    print(q03_is_palindrome("a"))               # True
    print(q03_is_palindrome(""))                # True (empty string)

    # Not palindromes
    print(q03_is_palindrome("hello"))           # False
    print(q03_is_palindrome("Python"))          # False
    print(q03_is_palindrome("Madam"))           # False (case-sensitive)
    print(q03_is_palindrome("nurses run"))      # False (spaces included)

