class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int max_profit = 0;
        int minimum = prices[0];
        for(int i = 1; i < n;i++){
            int profit = prices[i] - minimum;
            max_profit = max(max_profit,profit);
            minimum = min(minimum,prices[i]);
        }
        return max_profit;
    }
};