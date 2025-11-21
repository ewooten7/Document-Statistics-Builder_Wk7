"""
Homework 07: Library of Word Functions, all written recursively
===========================
Course:   CS 5001
Student:  Emmanuel Wooten

Various functions to practice recursion.
"""


def is_palindrome(word: str) -> bool:
    """
    Recursively looks at a string to determine if it is a palindrome.

    Does not remove punctuation or spaces, and assumes the word is
    already in lower case.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('hello')
        False
        >>> is_palindrome('girafarig')
        True
        >>> is_palindrome('farigaraf')
        True
        >>> is_palindrome('PizzaTime')
        False
        >>> is_palindrome('AcecA')
        True


    Args:
        word (str): the word to check

    Returns:
        bool: True if the word is a palindrome, False otherwise
    """
    # Base: empty string of single character
    if len(word) <= 1:
        return True

    # False: 1st and last characters DON'T Match
    if word[0] != word[-1]:
        return False

    # Rec: STRIP outer and check REST
    return is_palindrome(word[-1:1])


# Thinking:
"""
    EQ: Is there a catch-all function I can try to write that will help me solve this solution? 
    EQ: What is a 'palindrome', and how to represent in Python?
    Asking myself this helped me create different answers, which I had to drill into to consider how to represent in code. Recursion never fails to surprise me with its efficiency.
"""


def count_vowels(word: str) -> int:
    """
    Recursively counts the number of vowels in a string. Case
    does not matter.

    Examples:
        >>> count_vowels('hello')
        2
        >>> count_vowels('aeiou')
        5
        >>> count_vowels('AEIOU')
        5
        >>> count_vowels('GonFreecs')
        3
        >>> count_vowels('KilluaZoldyck')
        4
        >>> count_vowels('LeorioPaladinight')
        8



    Args:
        word (str): the word to check

    Returns:
        int: the number of vowels in the word
    """
    if word == "":
        return 0

    first = word[0].lower()
    rest = word[1:]

    vowels = "aeiou"

    if first in vowels:
        return 1 + count_vowels(rest)

    return count_vowels(rest)


def clean_word(word: str) -> str:
    """
    Recursively removes punctuation from a word, and reduces it to lower case.

    Examples:
        >>> clean_word('Hello!')
        'hello'
        >>> clean_word('World...')
        'world'
        >>> clean_word("!!!")
        ''
        >>> clean_word("H3ll0!!!")
        'h3ll0'
        >>> clean_word("...Python??")
        'python'
        >>> clean_word("NeO")
        'neo'

    See:
        https://docs.python.org/3/library/stdtypes.html#str.isalnum


    Args:
        word (str): the word to remove punctuation from

    Returns:
        str: the word without punctuation
    """
    if len(word) == 0:
        return ""

    first = word[0]
    rest = word[1:]

    if first.isalnum():
        return first.lower() + clean_word(rest)

    return clean_word(rest)


# Just running this file will run the doctests
if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)
