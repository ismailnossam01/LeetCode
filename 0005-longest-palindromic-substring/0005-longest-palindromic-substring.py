class Solution:
    def expand(i,j,s):
        left,right = i,j
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1 
        return s[left+1:right]
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        n = len(s)
        for i in range(n):
            odd = Solution.expand(i,i,s)
            if len(odd) > len(ans):
                ans = odd 
            even = Solution.expand(i,i+1,s) 
            if len(even) > len(ans):
                ans = even 
        return ans