"""
Count the number of occurrences of a specific character in a string.

Example:
>>> q08_count_char("example", "e")
2

>>> q08_count_char("banana", "a")
3

>>> q08_count_char("banana", "b")
1

>>> q08_count_char("banana", "x")
0  # character not found

>>> q08_count_char("", "a")
0  # empty string

>>> q08_count_char("Mississippi", "s")
4

>>> q08_count_char("Mississippi", "i")
4

>>> q08_count_char("Hello World", "l")
3

>>> q08_count_char("Hello World", " ")
1  # space counts as a character
"""


def q08_count_char(s:str,char:str)-> int:
    count = 0
    for x in s:
        if x == char:
            count += 1
    return count        


if __name__ == "__main__":
    print(q08_count_char("Mississippi", "s"))
