class Solution:
    def myAtoi(self, s: str) -> int:
        number = ''
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        sign = True  # positive
        hasSign = False
        for letter in s:
            if letter == ' ' and not hasSign:
                continue
            elif letter == '0' and number == '':
                hasSign = True
                continue
            elif letter >= '0' and letter <= '9':
                number += letter
                hasSign = True
            elif letter == '-' and not hasSign:
                sign = False  # negative
                hasSign = True
            elif letter == '+' and not hasSign:
                sign = True
                hasSign = True
            else:
                break
        if number == '':
            return '0'
        if sign:
            if int(number) > INT_MAX:
                return INT_MAX
            else:
                return number
        else:
            if int('-' + number) < INT_MIN:
                return INT_MIN
            else:
                return '-' + number
