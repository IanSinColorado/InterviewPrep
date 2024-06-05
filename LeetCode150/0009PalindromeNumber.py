class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        stack = []
        while x > 9:
            new_num = x % 10
            x -= new_num
            x /= 10
            x = int(x)
            stack.append(new_num)

        l = 0
        r = len(stack) - 1

        
        if len(stack) % 2 == 0:
            while l < r:
                if stack[l] != stack[r]:
                    return False
                l += 1
                r -= 1
        else:
            mid = int(len(stack) / 2)
            while l != mid:
                if stack[l] != stack[r]:
                    return False
                l += 1
                r -= 1

        return True