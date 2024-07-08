#include <vector>
using namespace std;

// Use and compare two hash tables
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        int hashTable1[1001] = { 0 };
        int hashTable2[1001] = { 0 };
        vector<int> ret;
        
        for(int i = 0; i < nums1.size(); ++i) {
            hashTable1[nums1[i]] += 1;
        }

        for (int i = 0; i < nums2.size(); ++i) {
            hashTable2[nums2[i]] += 1;
        }

        for(int i = 0; i < 1001; ++i) {
            if (hashTable1[i] > 0) {
                if(hashTable1[i] > hashTable2[i]) {
                    for(int j = 0; j <= hashTable2[i]; ++j) {
                        ret.push_back(i);
                    }
                } else {
                    for(int j = 0; j <= hashTable1[i]; ++j) {
                        ret.push_back(i);
                    }
                }
            }
        }
        return ret;
    }
};


// Use two pointers
// Go through both arrays and increment the pointers
// If the pointers ever point to the same number, add that numebr to the return array
//   and increment both pointers (as that element in both arrays has been "seen" by the pointers)
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        vector<int> ret;
        int l = 0;
        int r = 0;
        
        while(l < nums1.size() && r < nums2.size()) {
            if (nums1[l] < nums2[r]) {
                l += 1;
            } else if (nums1[l] > nums2[r]) {
                r += 1;
            } else {
                ret.push_back(nums1[l]);
                r += 1;
                l += 1;
            }
        }

        return ret;
    }
};