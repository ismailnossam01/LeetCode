class Solution {
public:
    int helperfunction(vector<int> & nums, int k){
        int n = nums.size();
        int count = 0;
        int i = 0, j = 0;
        unordered_map<int,int>m;
        while(j < n){
            m[nums[j]] += 1;
            while(m.size() == k){
                count += n - j;
                m[nums[i]] -= 1;
                if(m[nums[i]] == 0) m.erase(nums[i]);
                i += 1;
            }
            j += 1;
        }
        return count;
    }
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return helperfunction(nums,k) - helperfunction(nums,k+1);
    }
};