class Solution {
public:
    int f(vector <int>& arr, int k){
        if(k < 0) return 0;
        int n = arr.size();
        int i = 0, j = 0, ans = 0, sum = 0;
        while (j < n){
            sum += arr[j];
            while(sum > k){
                sum -= arr[i];
                i++;
            }
            ans += j - i + 1;
            j++;
        }
        return ans;
    }
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return f(nums,goal) - f(nums,goal-1);
    }
};