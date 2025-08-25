"""
Check if a string starts with a given prefix and ends with a given suffix.

Example:
>>> q15_check_start_end("example", prefix="ex", suffix="ple")
True
>>> q15_check_start_end("example", prefix="ex", suffix="amp")
False
>>> q15_check_start_end("hello world", prefix="he", suffix="ld")
True
>>> q15_check_start_end("hello world", prefix="wo", suffix="ld")
False
>>> q15_check_start_end("data", prefix="da", suffix="ta")
True
"""


def q15_check_start_end(s:str, prefix:str, suffix:str) -> bool:
    return s.startswith(prefix) and s.endswith(suffix)

if __name__ == "__main__":
    print( q15_check_start_end("data", prefix="da", suffix="ta"))
