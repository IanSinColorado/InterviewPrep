class Solution(object):
    def findSucc(self, hand, groupSize, i, n):
        findNum = hand[i] + 1
        count = 1
        hand[i] = -1
        i += 1

        while i < n and count < groupSize:
            if hand[i] == findNum:
                findNum += 1
                hand[i] = -1
                count += 1
            i += 1
        return count == groupSize

    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        hand = sorted(hand)
            
        for i in range(n):
            if hand[i] >= 0:
                if not self.findSucc(hand, groupSize, i, n):
                    return False

        return True
                