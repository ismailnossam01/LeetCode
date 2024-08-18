class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.split()
        r = last[-1]
        return len(r)