# Description:

# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters, - each taken only once - coming from s1 or s2.

# Examples:

# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(s1, s2):
    result = set()
    for char in s1:
        result.add(char)
    for char in s2:
        if char not in result:
            result.add(char)
    longest_str = "".join(sorted(result))
    return longest_str
