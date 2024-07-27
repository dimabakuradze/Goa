
"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def vowel_count(text):
    count = 0
    for i in text:
        if i in "aeiou":
            count+=1
    return f"{text} in your name is {count} vowels"
