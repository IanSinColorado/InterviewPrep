class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        storage = {}
        index = 0
        if len(words) != len(pattern):
            return False

        while index < len(words):
            if pattern[index] not in storage.keys():
                if words[index] in storage.values():
                    return False
                storage[pattern[index]] = words[index]
            else:
                if words[index] != storage[pattern[index]]:
                    return False
            index += 1
        print(storage)
        print(words)
        return True


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sIndex = 0
        storage = {}

        for pIndex in range(len(pattern)):
            key = pattern[pIndex]
            word = ""
            while sIndex < len(s) and s[sIndex] != " ":
                word += s[sIndex]
                sIndex += 1
            sIndex += 1

            if key in storage.keys():
                if storage[key] != word:
                    return False
            else:
                if word in storage.values():
                    return False
                storage[key] = word
        if sIndex != len(s)+1:
            return False
        return True