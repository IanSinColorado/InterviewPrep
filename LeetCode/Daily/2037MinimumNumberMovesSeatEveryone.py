class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        n = len(seats)

        seats = sorted(seats)
        students = sorted(students)

        cost = 0

        for i in range(n):
            if students[i] != seats[i]:
                cost += abs(students[i] - seats[i])
        
        return cost