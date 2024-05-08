class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        answer = sorted(zip(score, range(len(score))), key=lambda x: x[0], reverse=True)
        # print(answer)
        if len(score) >= 1:
            answer[0] = ('Gold Medal', answer[0][1])
        if len(score) >= 2:
            answer[1] = ('Silver Medal', answer[1][1])
        if len(score) >= 3:
            answer[2] = ('Bronze Medal', answer[2][1])
        if len(score) >= 4:
            for i in range(3, len(score)):
                answer[i] = (str(i + 1), answer[i][1])
                # print(i)
        # print(answer)
        # print(sorted(answer, key=lambda x: x[1]))
        out = []
        for a in sorted(answer, key=lambda x: x[1]):
            out.append(a[0])
        
        # print(out)
        return out
    
# Runtime: 61 ms, beats 45.14% 
# Memory: 12.81 MB, beats 18.40%