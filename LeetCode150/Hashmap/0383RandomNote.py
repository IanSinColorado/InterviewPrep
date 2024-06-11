class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import defaultdict
        ran_dict = defaultdict(int)
        mag_dict = defaultdict(int)

        for i in range(len(ransomNote)):
            ran_dict[ransomNote[i]] += 1

        for j in range(len(magazine)):
            mag_dict[magazine[j]] += 1

        ran_keys = list(ran_dict.keys())
        for i in range(len(ran_dict.keys())):
            if ran_dict[ran_keys[i]] < mag_dict[ran_keys[i]]:
                return False
            
        return True