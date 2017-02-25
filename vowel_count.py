
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, and u as vowels for this Kata.

def getCount(inputStr):
    """return the number of vowels in input string.

    >>> getCount("abracadabra")
    5

    """

    num_vowels = 0
    for char in inputStr:
        if char in ["a","e","i","o","u"]:
            num_vowels += 1
    return num_vowels
