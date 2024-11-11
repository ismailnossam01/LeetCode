class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                k += 1
            else:
                i += 1
        