class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        rev = str_x[::-1]
        if str_x == rev:
            return True 
        else:
            return False