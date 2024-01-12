from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # Attempt after seeing a solution and learning that it is sorted(list) and not list.sort()
        
        # make a map or hash table for sorted strings
        # using Python built in data structures
        wordMap = dict()

        for i in range(len(strs)):
            sortedWord = str(sorted(strs[i]))

            if sortedWord in wordMap.keys():
                wordMap[sortedWord].append(strs[i])
            else:
                wordMap[sortedWord] = [strs[i]]

        return list(wordMap.values())




        '''
        # Fail
        # make every word a unique string/hash
        # count the number of hashs
        hashs = []
        for i in range(len(strs)):
            string = list(strs[i]).sort()
            hash = defaultdict(int)

            for j in range(len(string)):
                hash[string[j]] += 1

            hashs.append(hash)

        # make the dictionaries into hashable items
        hashWords = []
        for i in range(len(hashs)):
            hash = ""

            keys = hashs[i].keys()
            vals = hashs[i].vals()

            for j in range(len(keys)):
                hash += keys[j]
                hash += vals[j]

            hashWords.append(hash)

        hashCounts = dict()
        for i in range(len(hashWords)):
            if hashWords[i] in hashCounts.keys():
                hashCounts[hashWords[i]].append(i)
            else:
                hashCounts[hashWords[i]] = [i]

        listOfLists = list()

        for numList in hashCounts.values():
            wordList = list()
            for num in numList:
                wordList.append(strs[num])

            listOfLists.append(wordList)

        return listOfLists
        '''

'''
# NeetCode solution
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
'''

'''
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''