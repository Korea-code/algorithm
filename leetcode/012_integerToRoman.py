class Solution:
    def intToRoman(self, num: int) -> str:
        M = num // 1000
        num %= 1000
        C = num // 100
        num %= 100
        X = num // 10
        num %= 10
        I = num

        number = ""
        for i in range(M):
            number += "M"
        if C == 9:
            number += "CM"
        elif C == 4:
            number += "CD"
        elif C >= 5:
            C -= 5
            number += "D"
            for i in range(C):
                number += "C"
        else:
            for i in range(C):
                number += "C"
        if X == 9:
            number += "XC"
        elif X == 4:
            number += "XL"
        elif X >= 5:
            X -= 5
            number += "L"
            for i in range(X):
                number += "X"
        else:
            for i in range(X):
                number += "X"
        if I == 9:
            number += "IX"
        elif I == 4:
            number += "IV"
        elif I >= 5:
            I -= 5
            number += "V"
            for i in range(I):
                number += "I"
        else:
            for i in range(I):
                number += "I"
        return number
