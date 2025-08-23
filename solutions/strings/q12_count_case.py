"""
Count the number of uppercase and lowercase letters in a string.

Example:
>>> q12_count_case("Example")
(1, 6)   # "E" is uppercase, rest are lowercase

>>> q12_count_case("HELLO")
(5, 0)   # all uppercase

>>> q12_count_case("hello")
(0, 5)   # all lowercase

>>> q12_count_case("Hello World")
(2, 8)   # "H" and "W" uppercase, rest lowercase (spaces ignored)

>>> q12_count_case("Python3")
(1, 5)   # "P" uppercase, "ython" lowercase, digit ignored

>>> q12_count_case("12345")
(0, 0)   # only digits, no letters

>>> q12_count_case("")
(0, 0)   # empty string edge case
"""

def q12_count_case(s:str)-> tuple:
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower+=1
    return (upper, lower)


if __name__ == "__main__":
    print(q12_count_case("Hello World"))
