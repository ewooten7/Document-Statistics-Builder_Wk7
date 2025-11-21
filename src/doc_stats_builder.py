"""
Homework 07: Document Statistics Builder
===========================
Course:   CS 5001
Student:  Emmanuel Wooten

Functions for reading document stats. They all assume a 'document' is
a tuple or list of strings, where each string is a line of the document.

For example:
    ('Hello', 'World') is the document
    Hello
    World


    ('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho')
    An old silent pond...
    A frog jumps into the pond—
    Splash! Silence again.
    - Matsuo Basho

"""

from word_lib import clean_word, count_vowels, is_palindrome


def get_number_lines(lines: tuple) -> int:
    """
    Gets the number of lines in the document.

    Examples:
        >>> get_number_lines(('Hello', 'World'))
        2
        >>> get_number_lines(('Goodbye', 'World'))
        2
        >>> get_number_lines(('My', 'name', 'is', 'Yoshikage', 'Kira'))
        5
        >>> get_number_lines(('こんにちは', '世界'))
        2
        >>> get_number_lines(('TUNG TUNG TUNG TUNG TUNG TUNG SAHUR',))
        1
        >>> get_number_lines(('Piplup', 'Lv5', 'Ability:Torrent'))
        3


    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of lines in the document
    """
    return len(lines)


# Thinking:
"""
This was super easy. AND I am getting much better with making edge cases!
I never considered using other languages for doctests before, and this one
is particually relevant in trying this out! I think the haiku from Basho made me think about this. I used to read his works in middle school!
"""


def get_number_words(lines: tuple) -> int:
    """
    Gets the number of words in the document.
    Note, make sure to clean the words before counting them,
    and an 'empty' word should not be counted.

    Examples:
        >>> get_number_words(('Hello', 'World'))
        2
        >>> get_number_words(('Aloha!', '-', 'World'))
        2
        >>> get_number_words(('Hello!!!', '...'))
        1
        >>> get_number_words(('mañana', 'niño'))
        2
        >>> get_number_words(('🔥🔥🔥',))
        0
        >>> get_number_words(('Supercalifragilistic', 'expialidocious', 'even', 'though' , 'the', 'sound', 'of', 'it', 'sounds', 'quite', 'atrocious'))
        11
        >>> get_number_words(('!!!!!!!!!!!!'))
        0


    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of words in the document
    """
    count = 0

    for line in lines:
        words = line.split()
        for word in words:
            w_cleaned = clean_word(word)
            if w_cleaned != '':
                count += 1

    return count


# Thinking:
"""
Seemed straightforward at first, except I kept getting an error on line 53 with test failing. 
Turns out, I forgot to add the return statement! This makes my function implicitly return NONE.
Hence: Failed example:
    get_number_words(('Aloha!', '-', 'World'))
Expected:
    2
Got nothing.

Also, I'm getting bolder with edge cases. Why not use emojis?
"""


def get_vowel_count(lines: tuple) -> int:
    """
    Gets the number of vowels in the document.

    Examples:
        >>> get_vowel_count(('Hello', 'World'))
        3

        >>> get_vowel_count(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        24

        >>> get_vowel_count(("I'm gonna make him an offer he can't refuse.",))
        14

        >>> get_vowel_count(("E.T. phone home",))
        5

        >>> get_vowel_count(('Oh? You’re approaching me? Instead of running away, you’re coming right to me? Even though your grandfather, Joseph, told you the secret of The World, like an exam student scrambling to finish the problems on an exam until the last moments before the chime?'))
        76

        >>> get_vowel_count(('I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character'))
        49

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of vowels in the document
    """
    total = 0

    for line in lines:
        words = line.split()
        for word in words:
            w_cleaned = clean_word(word)
            total += count_vowels(w_cleaned)

    return total


# Thinking
"""
Another case: also thought this was easy, but ran into another syntax error:
"UnboundLocalError: cannot access local variable 'total' where it is not associated with a value"
This meant I referenced a local variable (total) WITHOUT first defining it OUTSIDE the function
(I did this with the others with "count", but total forgot again to put it here).
"""


def get_word_palindromes(lines: tuple) -> int:
    """
    Gets the number of palindromes in the document. Ignores punctuation.

    Examples:
        >>> get_word_palindromes(('Hello', 'World'))
        0

        >>> get_word_palindromes(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        1

        >>> get_word_palindromes(('raceCar', 'kayak!', 'sator arepo tenet opera rotas!'))
        3

        >>> get_word_palindromes(('A b c d e f g h i j k elemeno p',))
        12

        >>> get_word_palindromes(('Super Mario Racecar on sale!',))
        1

        >>> get_word_palindromes(('!!@#&%$@!*()@#&!@'))
        0

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of palindromes in the document
    """
    count = 0

    for line in lines:
        words = line.split()
        for word in words:
            w_cleaned = clean_word(word)
            if w_cleaned != '' and is_palindrome(w_cleaned):
                count += 1

    return count


def get_sentence_palindromes(lines: tuple) -> int:
    """
    Gets the number of palindromes in the document. Ignores punctuation.

    Examples:
        >>> get_sentence_palindromes(('Hello', 'World'))
        0

        >>> get_sentence_palindromes(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        0

        >>> get_sentence_palindromes(('A raceCar', 'A kayak!', 'sator arepo tenet opera rotas!'))
        1

        >>> get_sentence_palindromes(('A'))
        1

        >>> get_sentence_palindromes(('REfeR', 'to', 'Me'))
        1

        >>> get_sentence_palindromes(('CiVic', 'Duties'))
        1

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of palindromes in the document
    """
    count = 0

    for line in lines:
        w_cleaned = clean_word(line)
        if len(w_cleaned) > 1 and is_palindrome(w_cleaned):
            count += 1

    return count

#Thinking
"""
This was a good one! The autograder got me here: "4.0) Approaching: Tests the number of palindromes that exist on a word basis."
On line 241, I changed, w_cleaned != '', to a better if len(w_cleaned) > 1, meaning that the resulted clean should be at LEAST 2 characters long before I consider it a valid “word” for palindrome checking.
"""


# just running the file will automatically run doctest
if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)
