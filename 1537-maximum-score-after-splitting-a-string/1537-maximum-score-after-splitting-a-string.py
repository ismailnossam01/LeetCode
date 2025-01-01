class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        res_arr = []
        for i in range(1,n):
            left = s[:i]
            right = s[i:]
            left_zeros = 0
            right_ones = 0
            for i in left:
                if i == '0':
                    left_zeros += 1 
            for i in right:
                if i == '1':
                    right_ones += 1 
            res_arr.append(left_zeros + right_ones) 
        return max(res_arr)
            
