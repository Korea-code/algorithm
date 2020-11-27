class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        if len(strs) == 0:
            return commonPrefix
        if len(strs) == 1:
            return strs[0]
        if strs[0] == "":
            return ""

        for word in strs:
            if commonPrefix == "":
                commonPrefix = word
            else:
                i = 0
                while(i < len(word) and i < len(commonPrefix) and word[i] == commonPrefix[i]):
                    i += 1
                if i == 0:
                    return ""
                else:
                    commonPrefix = word[:i]
        return commonPrefix
