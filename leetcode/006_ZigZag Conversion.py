class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1 or len(s) == 2 or numRows == 1:
            return s
        arr = []
        result = ""
        for i in range(numRows):
            arr.append("")
        for i in range(len(s)):
            if i % (numRows * 2 - 2) < numRows:
                arr[i % (numRows * 2 - 2)] += s[i]
            else:
                arr[2 * numRows - i % (numRows * 2 - 2) - 2] += s[i]
        for string in arr:
            result += string
        return result
