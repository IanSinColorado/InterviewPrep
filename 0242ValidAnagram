class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_dict = dict()
        t_dict = dict()

        for i in s:
            if i in list(s_dict.keys()):
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for i in t:
            if i in list(t_dict.keys()):
                t_dict[i] += 1
            else:
                t_dict[i] = 1

        if len(s_dict.keys()) != len(t_dict.keys()):
            return False
        
        # print(list(s_dict.values()))
        # print(list(t_dict.values()))
        t_dict_vals = list(t_dict.values())
        t_dict_keys = list(t_dict.keys())
        s_dict_keys = list(s_dict.keys())

        for i,val in enumerate(list(s_dict.values())):
            if val != t_dict_vals[i]:
                return False
            
            if t_dict_keys[i] != s_dict_keys[i]:
                return False


        return True

# From LeetCode Solutions
# HASH TABLE SOLUTION
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        
        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1
        
        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1
        
        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False
        
        return True
'''