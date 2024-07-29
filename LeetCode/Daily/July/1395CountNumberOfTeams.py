# Greedy Solution:
# Find the middle element of the groups of three
# find the num of elements that are lower to the left
# find the num of elements that are higher to the right
# find combinations
# do it for the other way
# Add all combinations
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ret = 0

        for i in range(1, len(rating)):
            left_lower = 0
            right_upper=  0
            # left_upper=  0
            # right_lower = 0 
            for l in range(0, i):
                if rating[l] < rating[i]:
                    left_lower += 1
                # else:
                    # left_upper += 1
            for r in range(i+1, len(rating)):
                if rating[r] > rating[i]:
                    right_upper += 1
                # else:
                    # right_lower += 1

            ret += (left_lower * right_upper) + ((i+1 - left_lower) * (i+1 - right_upper))

        return ret
    
