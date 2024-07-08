# include <vector>
using namespace std;

class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int counter = 0;
        for(int i = 0; i < arr.size(); ++i) {
            if (arr[i] % 2 == 0) {
                counter = 0;
            } else {
                if (counter == 2){
                    return true;
                }
                counter += 1;
            }
        }
        return false;
    }
};