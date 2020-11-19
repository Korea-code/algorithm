class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        maxLen = -1
        for i in range(len(s)):
            j, k = i, i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if maxLen < k - j + 1:
                    maxLen = k - j + 1
                    palindrome = s[j: k + 1]
                j -= 1
                k += 1
            j, k = i, i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if maxLen < k - j + 1:
                    maxLen = k - j + 1
                    palindrome = s[j: k + 1]
                j -= 1
                k += 1

        return palindrome
