
"""
Check for Balanced Parentheses


4

Problem Statement: Check Balanced Parentheses. Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false. .

Note:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Examples
Example 1:
Input: str = “( )[ { } ( ) ]”
Output: True
Explanation: As every open bracket has its corresponding close bracket. Match parentheses are in correct order hence they are balanced.


Example 2:
Input: str = “[ ( )”
Output: False
Explanation: As ‘[‘ does not have ‘]’ hence it is not valid and will return false.

"""


def first_approach(text_string):
    stack = []

    for char in text_string:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            peek = stack[-1]
            if (char == ')' and peek == '(') or (char == ']' and peek == '[') or (char == '}' and peek == '{'):
                stack.pop()
            else:
                return False
    return len(stack) == 0


print("current string is balanced parentheses : ",first_approach(text_string="([{([)}])"))