# In English and programming, groups can be made using symbols such as "()" and "{}" that change meaning. However, these groups must be closed in the correct order to maintain correct syntax.

# Your job in this kata will be to make a program that checks a string for correct grouping. For instance, the following groups are done correctly:

# ({})
# [[]()]
# [{()}]
# The next are done incorrectly

# {(})
# ([]
# [])
# A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.

# Your function will take an input string that may contain any of the symbols "()" "{}" or "[]" to create groups.

# It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.

class Stack(object):
    """creating a stack class for later use"""
    def __init__(self):
        self.stack = []

    def push(self,item):

        self.stack.append(item)

    def pop(self):

        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

def check_parans(str):
    """using a stack to keep track of the correct pairs of paranthesis.

    >>> check_parans("{({)")
    False
    >>> check_parans("[{()}]")
    True

    """

    stack = Stack()
    isBalanced = True
    index = 0
    while isBalanced and index < len(str):
        char = str[index]
        if char in "({[":
            stack.push(char)
        else:
            if stack.isEmpty():
                isBalanced = False
            else:
                stack.pop()
        index += 1

    if stack.isEmpty() and isBalanced:
        return True
    else:
        return False
