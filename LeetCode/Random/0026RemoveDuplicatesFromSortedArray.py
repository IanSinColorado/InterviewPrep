class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        storage = set()
        n = len(nums)
        i = 0
        unique = 0
        while i < n:
            # print(i)
            if nums[i] in storage:
                # move all of the other numbers up one space
                # print(n-1)
                # print(i)
                nums.pop(i)
                # for j in range(i, n-1):
                #     nums[j] = nums[j+1]
                i -= 1
                n -= 1
            else:
                storage.add(nums[i])
                unique += 1
            i += 1

        return unique

# They are in order
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # -100 <= nums[i] <= 100
        unique_elem = nums[0]
        i = 1
        n = len(nums)
        while i < n:
            if nums[i] != unique_elem:
                unique_elem = nums[i]
                i += 1
            else:
                nums.pop(i)
                n -= 1

        return len(nums)
    
class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        slow_pointer = 0
        for fast_pointer in range(len(nums)):
            if nums[fast_pointer] != nums[slow_pointer]:
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_pointer]

        return slow_pointer
        
