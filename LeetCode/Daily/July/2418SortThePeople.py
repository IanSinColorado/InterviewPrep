class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        peopleDict = [[names[i], heights[i]] for i in range(len(names))]

        return [sorted(peopleDict, key=lambda x: x[1], reverse=True)[i][0] for i in range(len(names))]