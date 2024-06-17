class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sHash = {}
        for i in range(len(s)):
            if s[i] in sHash:
                if sHash[s[i]] != t[i]:
                    return False
            else:
                sHash[s[i]] = t[i]

        return True
