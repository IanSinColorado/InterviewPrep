class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        roadDict = defaultdict(int)
        rank = [0] * n
        total = 0
        for i in range(len(roads)):
            for j in roads[i]:
                roadDict[j] += 1

        for index, item in enumerate(sorted(list(dict(roadDict).items()), key=lambda x: x[1], reverse=True)):
            rank[item[0]] = n-index

        for i in range(len(roads)):
            for j in roads[i]:
                total += rank[j]

        return total