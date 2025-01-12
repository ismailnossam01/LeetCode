class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = right = 0 
        ans = 0
        zeros = 0  
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1 
            while zeros > 0:
                if nums[left] == 0: 
                    zeros -= 1
                left += 1
            ans = max(right-left+1,ans)
            right += 1
        return ans           