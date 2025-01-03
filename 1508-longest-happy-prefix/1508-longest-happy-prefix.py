class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        i = 0
        j = 1

        while j < n:
            if s[i] == s[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]

        return s[:lps[n - 1]]