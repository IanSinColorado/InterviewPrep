class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        distance = 1
        for i in range(len(nums)-2, -1, -1):
            print(nums[i])
            print(distance)
            if nums[i] >= distance:
                distance = 1
            else:
                distance += 1

        if distance != 1:
            return False
        else:
            return True
        

