class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int left = 0, right = 0;
    int numZeroes = 0, longestSeq = 0;

    while (right < nums.size()) {
        if (nums[right] == 0) {
            numZeroes++;
        }

        while (numZeroes > 0) {
            if (nums[left] == 0) {
                numZeroes--;
            }
            left++;
        }

        longestSeq = max(longestSeq, right - left + 1);
        right++;
    }

    return longestSeq;
        

    }
};