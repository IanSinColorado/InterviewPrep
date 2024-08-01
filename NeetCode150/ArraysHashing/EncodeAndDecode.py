class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in range(len(strs)):
            ret += str(len(strs[i])) + "#" + strs[i]

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i + length

            ret.append(s[i:j])

        return ret