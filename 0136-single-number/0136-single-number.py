class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            c = nums.count(i)
            if c == 1:
                return i
        