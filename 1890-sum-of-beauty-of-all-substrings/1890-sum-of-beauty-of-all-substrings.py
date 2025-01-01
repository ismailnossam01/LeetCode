class Solution:
    def beauty(arr):
        mini = float('inf')
        maxi = 0 
        for i in range(26):
            if arr[i] != 0:
                mini = min(mini,arr[i])
                maxi = max(maxi,arr[i])
        return maxi - mini 

    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0 
        for i in range(n):
            arr = [0] * 26 
            for j in range(i,n):
                arr[ord(s[j]) - ord('a')] += 1 
                ans += Solution.beauty(arr) 
        return ans
        