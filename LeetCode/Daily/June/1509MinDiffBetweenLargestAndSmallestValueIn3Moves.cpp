#include <vector>
using namespace std;

class Solution {
public:
    int minDifference(vector<int>& nums) {
        if (nums.size() <= 4) {
            return 0;
        }

        sort(nums.begin(), nums.end());
        
        int n = nums.size()-1;
        int minimum = min(nums[n] - nums[3], nums[n-1] - nums[2]);
        minimum = min(minimum, nums[n-2] - nums[1]);
        return min(minimum, nums[n-3] - nums[0]);
        // return min(nums[n] - nums[3], nums[n-1] - nums[2], nums[n-2] - nums[1], nums[n-3] - nums[0]);

    }
};