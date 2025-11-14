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

    Args:
        word (str): the word to check

    Returns:
        bool: True if the word is a palindrome, False otherwise
    """
    pass


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

    Args:
        word (str): the word to check

    Returns:
        int: the number of vowels in the word
    """
    pass


def clean_word(word: str) -> str:
    """
    Recursively removes punctuation from a word, and reduces it to lower case.

    Examples:
        >>> clean_word('Hello!')
        'hello'
        >>> clean_word('World...')
        'world'

    See:
        https://docs.python.org/3/library/stdtypes.html#str.isalnum


    Args:
        word (str): the word to remove punctuation from

    Returns:
        str: the word without punctuation
    """
    pass


# Just running this file will run the doctests
if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)
