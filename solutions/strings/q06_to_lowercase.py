"""
Convert a string to lowercase without using str.lower().

Example:
>>> q06_to_lowercase("Example")
'example'

>>> q06_to_lowercase("PYTHON")
'python'

>>> q06_to_lowercase("Hello World!")
'hello world!'

>>> q06_to_lowercase("123 ABC xyz!")
'123 abc xyz!'

>>> q06_to_lowercase("")
''
"""

def q06_to_lowercase(s:str) -> str:
    lowercase = ""
    for char in s:
        if "A" <= char <= "Z": #check uppercase
            lowercase += chr(ord(char) + 32)
        else:
            lowercase += char
    return lowercase

if __name__ == "__main__":
    print(q06_to_lowercase("123 ABC xyz!"))
