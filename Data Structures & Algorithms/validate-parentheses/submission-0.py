class Solution:
    def isValid(self, s: str) -> bool:

        #dictionary

        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            #if it's a closing bracket
            if char in matching:
                #pop from stack
                top_element = stack.pop() if stack else '#'

                #check if matches the expected opening bracket
                if matching[char] != top_element:
                    return False
            else:
                #It's an opening bracket, push onto stack
                stack.append(char)
        return not stack

        