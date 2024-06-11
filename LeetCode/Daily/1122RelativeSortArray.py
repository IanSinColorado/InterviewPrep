# Hash Map Solution
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        hashMap = {k: i for i, k in enumerate(arr2)}

        # sort the array in a way where the rank is first determined by 
        # its hashmap index, then its number left over
        # max value is 1000, so adding 1000 to it automatically makes the key go to any rank
        # above any key in arr2
        
        return sorted(arr1, key=lambda a: hashMap.get(a, 1000+a))


# Clever list manupulation
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in arr2:
            # remove elements from arr1 and add them 
            # to the return array in the order they are in arr2
            while i in arr1:
                arr1.remove(i)
                arr.append(i)

        # Copy the remaining elements, those found in arr1, but not arr2
        # and sort them. Then add them to the end of the return array
        arr.extend(sorted(arr1[:]))
        return arr
        