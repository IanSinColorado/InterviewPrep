class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == '[':
                stack.append('[')
            elif s[i] == '(':
                stack.append('(')
            elif s[i] == '{':
                stack.append('{')
            elif s[i] == ']':
                if len(stack) == 0 or '[' != stack.pop():
                    return False
            elif s[i] == ')':
                if len(stack) == 0 or '(' != stack.pop():
                    return False
            elif s[i] == '}':
                if len(stack) == 0 or '{' != stack.pop():
                    return False

        if len(stack) == 0:
            return True
        return False

