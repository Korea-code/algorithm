class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        prev = ""
        for num in s:
            if num == "M":
                if prev == "C":
                    number += 800
                else:
                    number += 1000
            elif num == "D":
                if prev == "C":
                    number += 300
                else:
                    number += 500
            elif num == "C":
                if prev == "X":
                    number += 80
                else:
                    number += 100
            elif num == "L":
                if prev == "X":
                    number += 30
                else:
                    number += 50
            elif num == "X":
                if prev == "I":
                    number += 8
                else:
                    number += 10
            elif num == "V":
                if prev == "I":
                    number += 3
                else:
                    number += 5
            elif num == "I":
                number += 1
            prev = num
        return number
