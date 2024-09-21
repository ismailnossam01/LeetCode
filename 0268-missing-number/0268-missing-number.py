class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        all_nums_in_range = []
        for i in range(nums_len+1):
            all_nums_in_range.append(i)
        for i in all_nums_in_range:
            if i not in nums:
                return i 
        

        