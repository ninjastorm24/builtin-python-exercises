"""
Check if a string contains only digits.

Example:
>>> q07_is_digit_string("12345")
True

>>> q07_is_digit_string("00123")
True

>>> q07_is_digit_string("123abc")
False

>>> q07_is_digit_string("example")
False

>>> q07_is_digit_string("123 456")
False  # spaces are not digits

>>> q07_is_digit_string("")
False  # empty string is usually considered not a digit string

>>> q07_is_digit_string("0")
True

>>> q07_is_digit_string("9876543210")
True

"""

def q07_is_digit_string(s:str) -> bool:
    return s.isdigit() and bool(s)
    

if __name__ == "__main__":
    print(q07_is_digit_string("123abc"))
