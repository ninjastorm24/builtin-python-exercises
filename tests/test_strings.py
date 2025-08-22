from solutions.strings.q01_reverse_string import q01_reverse_string
from solutions.strings.q02_count_vowels import q02_count_vowels
from solutions.strings.q03_is_palindrome import q03_is_palindrome
from solutions.strings.q04_count_words import q04_count_words
from solutions.strings.q05_to_uppercase import q05_to_uppercase
from solutions.strings.q06_to_lowercase import q06_to_lowercase
from solutions.strings.q07_is_digit_string import q07_is_digit_string
from solutions.strings.q08_count_char import q08_count_char
from solutions.strings.q09_remove_vowels import q09_remove_vowels
from solutions.strings.q10_most_frequent_char import q10_most_frequent_char
from solutions.strings.q11_is_anagram import q11_is_anagram
from solutions.strings.q12_count_case import q12_count_case
from solutions.strings.q13_remove_spaces import q13_remove_spaces
from solutions.strings.q14_replace_substring import q14_replace_substring
from solutions.strings.q15_check_start_end import q15_check_start_end
from solutions.strings.q16_count_consonants import q16_count_consonants
from solutions.strings.q17_unique_chars import q17_unique_chars
from solutions.strings.q18_remove_duplicates import q18_remove_duplicates
from solutions.strings.q19_is_pangram import q19_is_pangram
from solutions.strings.q20_count_sentences import q20_count_sentences
from solutions.strings.q21_longest_word import q21_longest_word
from solutions.strings.q22_is_alpha import q22_is_alpha
from solutions.strings.q23_count_digits import q23_count_digits
from solutions.strings.q24_string_to_list import q24_string_to_list
from solutions.strings.q25_reverse_words import q25_reverse_words


from solutions.strings.q01_reverse_string import q01_reverse_string
from solutions.strings.q02_count_vowels import q02_count_vowels

def test_q01_reverse_string():
    assert q01_reverse_string("hello") == "olleh"
    assert q01_reverse_string("Python") == "nohtyP"
    assert q01_reverse_string("") == ""  # empty string
    assert q01_reverse_string("a") == "a"  # single character
    assert q01_reverse_string("12345") == "54321"  # numbers in string

def test_q02_count_vowels():
    assert q02_count_vowels("example") == 3
    assert q02_count_vowels("hello world") == 3
    assert q02_count_vowels("xyz") == 0
    assert q02_count_vowels("AEIOU") == 5
    assert q02_count_vowels("Python Programming") == 4


def test_q03_is_palindrome():
    # Palindromes
    assert q03_is_palindrome("madam") is True
    assert q03_is_palindrome("racecar") is True
    assert q03_is_palindrome("a") is True
    assert q03_is_palindrome("") is True  # empty string edge case

    # Not palindromes
    assert q03_is_palindrome("hello") is False
    assert q03_is_palindrome("python") is False
    assert q03_is_palindrome("Madam") is False  # case-sensitive
    assert q03_is_palindrome("nurses run") is False  # spaces not ignored

def test_q04_count_words():
    # Normal cases
    assert q04_count_words("example") == 1
    assert q04_count_words("hello world") == 2
    assert q04_count_words("Python is fun") == 3
    
    # Leading/trailing/multiple spaces
    assert q04_count_words("   Leading and trailing spaces   ") == 4
    assert q04_count_words("Multiple    spaces between words") == 4
    
    # Tabs and newlines
    assert q04_count_words("New\nline and\ttab separated") == 5
    
    # Edge cases
    assert q04_count_words("") == 0
    assert q04_count_words("   ") == 0  # only spaces
    assert q04_count_words("\t\n") == 0  # only whitespace characters

def test_q05_to_uppercase():
    # TODO: Write test cases for q05_to_uppercase
    assert True  # placeholder

def test_q06_to_lowercase():
    # TODO: Write test cases for q06_to_lowercase
    assert True  # placeholder

def test_q07_is_digit_string():
    # TODO: Write test cases for q07_is_digit_string
    assert True  # placeholder

def test_q08_count_char():
    # TODO: Write test cases for q08_count_char
    assert True  # placeholder

def test_q09_remove_vowels():
    # TODO: Write test cases for q09_remove_vowels
    assert True  # placeholder

def test_q10_most_frequent_char():
    # TODO: Write test cases for q10_most_frequent_char
    assert True  # placeholder

def test_q11_is_anagram():
    # TODO: Write test cases for q11_is_anagram
    assert True  # placeholder

def test_q12_count_case():
    # TODO: Write test cases for q12_count_case
    assert True  # placeholder

def test_q13_remove_spaces():
    # TODO: Write test cases for q13_remove_spaces
    assert True  # placeholder

def test_q14_replace_substring():
    # TODO: Write test cases for q14_replace_substring
    assert True  # placeholder

def test_q15_check_start_end():
    # TODO: Write test cases for q15_check_start_end
    assert True  # placeholder

def test_q16_count_consonants():
    # TODO: Write test cases for q16_count_consonants
    assert True  # placeholder

def test_q17_unique_chars():
    # TODO: Write test cases for q17_unique_chars
    assert True  # placeholder

def test_q18_remove_duplicates():
    # TODO: Write test cases for q18_remove_duplicates
    assert True  # placeholder

def test_q19_is_pangram():
    # TODO: Write test cases for q19_is_pangram
    assert True  # placeholder

def test_q20_count_sentences():
    # TODO: Write test cases for q20_count_sentences
    assert True  # placeholder

def test_q21_longest_word():
    # TODO: Write test cases for q21_longest_word
    assert True  # placeholder

def test_q22_is_alpha():
    # TODO: Write test cases for q22_is_alpha
    assert True  # placeholder

def test_q23_count_digits():
    # TODO: Write test cases for q23_count_digits
    assert True  # placeholder

def test_q24_string_to_list():
    # TODO: Write test cases for q24_string_to_list
    assert True  # placeholder

def test_q25_reverse_words():
    # TODO: Write test cases for q25_reverse_words
    assert True  # placeholder

