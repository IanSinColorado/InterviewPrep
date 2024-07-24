# First solution i made; lots of memory usage
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappedNums = []
        for i in range(len(nums)):
            new_num = ""
            for j in range(len(str(nums[i]))):
                new_num += str(mapping[int(j)])
            mappedNums.append(int(new_num))

        ans = []
        for i in sorted(zip(nums, mappedNums), key=lambda x: x[1]):
            ans.append(i[0])

        return ans

# Second solution
# better usage of memory and HashTable
# Converts int to string, then back to int
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappedNums = {}
        for i in range(len(nums)):
            new_num = ""
            for j in str(nums[i]):
                new_num += str(mapping[int(j)])

            mappedNums[nums[i]] = int(new_num)

        nums.sort(key=lambda x: mappedNums[x])
        
        return nums
    
# Third Solution:
# Use modulo and division to convert the nums
# Hopefully speeds up as a result of math operations instead of string ones
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def translate_integer(integer: int):
            if integer == 0:
                return mapping[0]
            new_int: int = 0
            mult: int = 1
            while integer > 0:
                new_int = mapping[integer % 10] * mult + new_int
                integer //= 10
                mult *= 10
            return new_int
        
        rankMap = {}
        for i in range(len(nums)):
            rankMap[nums[i]] = translate_integer(nums[i])

        nums.sort(key=lambda x: rankMap[x])

        return nums
