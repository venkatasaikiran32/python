# string_utils.py

def reverse_string(s):
    """
    it returns the reverse  of the input string.
    """
    return s[::-1]

def capitalize_string(s):
    """
    it  caitalizes the first letter of each word in the input string.
    """
    return s.title()

def to_uppercase(s):
    """
    it converts the input string to uppercase.
    """
    return s.upper()

def to_lowercase(s):
    """
    it converts the input string to lowercase.
    """
    return s.lower()

def remove_whitespace(s):
    """
    it removes all whitespace from the input string.
    """
    return ''.join(s.split())

def replace_substring(s, old, new):
    """
    it replaces all occurrences of a substring with another substring.
    """
    return s.replace(old, new)

def split_string(s, delimiter=' '):
    """
    it splits the input string by the given delimiter.
    """
    return s.split(delimiter)

def join_strings(strings, delimiter=' '):
    """
    it joins a list of strings into one string with the given delimiter.
    """
    return delimiter.join(strings)

def strip_string(s):
    """
    it removes leading and trailing whitespace from the input string.
    """
    return s.strip()

def lstrip_string(s):
    """
    it removes leading whitespace from the input string.
    """
    return s.lstrip()

def rstrip_string(s):
    """
    it removes trailing whitespace from the input string.
    """
    return s.rstrip()

def starts_with(s, prefix):
    """
    it checks if the input string starts with the given prefix.
    """
    return s.startswith(prefix)

def ends_with(s, suffix):
    """
    it checks if the input string ends with the given suffix.
    """
    return s.endswith(suffix)

def is_alpha(s):
    """
    it checks if the input string contains only alphabetic characters.
    """
    return s.isalpha()

def is_digit(s):
    """
    it checks if the input string contains only digits.
    """
    return s.isdigit()

def is_alnum(s):
    """
    it checks if the input string contains only alphanumeric characters.
    """
    return s.isalnum()

def is_lower(s):
    """
    it checks if the input string contains only lowercase characters.
    """
    return s.islower()

def is_upper(s):
    """
    it checks if the input string contains only uppercase characters.
    """
    return s.isupper()

def count_substring(s, substring):
    """
    it counts the occurrences of a substring in the input string.
    """
    return s.count(substring)

def find_first(s, substring):
    """
    it finds the first occurrence of a substring in the input string.
    """
    return s.find(substring)

def find_last(s, substring):
    """
    it finds the last occurrence of a substring in the input string.
    """
    return s.rfind(substring)

def capitalize_first_letter(s):
    """
    it capitalizes the first letter of the input string.
    """
    return s.capitalize()

def swap_case(s):
    """
    it swaps the case of each character in the input string.
    """
    return s.swapcase()


def center_string(s, width, fillchar=' '):
    """
    it centers the input string in a field of the given width, using the specified fill character.
    """
    return s.center(width, fillchar)

def ljust_string(s, width, fillchar=' '):
    """
    it left-justifies the input string in a field of the given width, using the specified fill character.
    """
    return s.ljust(width, fillchar)

def rjust_string(s, width, fillchar=' '):
    """
    it right-justifies the input string in a field of the given width, using the specified fill character.
    """
    return s.rjust(width, fillchar)
