class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                confirm = True
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        confirm = False
                if confirm:
                    return i
        return -1
