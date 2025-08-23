"""
Remove all spaces from a string.

Example:
>>> q13_remove_spaces("example")
"example"   # no spaces → stays the same

>>> q13_remove_spaces("hello world")
"helloworld"   # spaces removed

>>> q13_remove_spaces("   leading spaces")
"leadingspaces"   # remove leading spaces

>>> q13_remove_spaces("trailing spaces   ")
"trailingspaces"  # remove trailing spaces

>>> q13_remove_spaces("  multiple   spaces  inside  ")
"multiplespacesinside"   # all spaces removed, not just trimmed

>>> q13_remove_spaces("")
""   # empty string stays empty

>>> q13_remove_spaces("no_space")
"no_space"   # underscore is not space, remains unchanged
"""


def q13_remove_spaces(s:str) -> str:
    str_list =  s.split()
    return "".join(str_list)

if __name__ == "__main__":
    print(q13_remove_spaces("trailing spaces   "))
