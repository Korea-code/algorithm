class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        if number != number[::-1]:
            return False
        else:
            return True
