"""
Convert a string to uppercase without using str.upper().

Examples:
>>> q05_to_uppercase("example")
"EXAMPLE"
>>> q05_to_uppercase("hello World")
"HELLO WORLD"
>>> q05_to_uppercase("Python123")
"PYTHON123"
>>> q05_to_uppercase("already UPPER")
"ALREADY UPPER"
>>> q05_to_uppercase("") 
""
>>> q05_to_uppercase("mixed CASE string")
"MIXED CASE STRING"
>>> q05_to_uppercase("numbers 123 and symbols !@#")
"NUMBERS 123 AND SYMBOLS !@#"
"""


def q05_to_uppercase(s:str) -> str:
    uppercase = ""
    for char in s:
        if "a" <= char <= "z": #check lowercase
            uppercase += chr(ord(char) - 32) #make uppercase
        else:
            uppercase += char
    return uppercase
    




if __name__ == "__main__":
    print(q05_to_uppercase("numbers 123 and symbols !@#"))
    print( q05_to_uppercase("hello World"))
