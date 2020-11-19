class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        result = 0
        current = 0
        for letter in s:
            if letter not in arr:
                arr.append(letter)
                current += 1
            else:
                index = arr.index(letter)
                del arr[: index + 1]
                arr.append(letter)
                current = len(arr)
            if current > result:
                result = current
        return result
