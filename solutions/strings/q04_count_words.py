"""
Count the number of words in a string.

Example:
>>> q04_count_words("example")
1
>>> q04_count_words("hello world")
2
>>> q04_count_words("Python is fun")
3
>>> q04_count_words("   Leading and trailing spaces   ")
4
>>> q04_count_words("") 
0
>>> q04_count_words("One-word")
1
>>> q04_count_words("Multiple    spaces between words")
4
>>> q04_count_words("New\nline and\ttab separated")
5
"""

def q04_count_words(s: str) -> int:
    return len(s.split())

if __name__ == "__main__":
    print(q04_count_words("   Leading and trailing spaces   "))
