class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        countCounter = 1
        first = True
        negative = False
        counter = 0
        _dividend = dividend
        _divisor = divisor

        if (_dividend < 0 and _divisor > 0) or (_dividend > 0 and _divisor < 0):
            negative = True
        _dividend = abs(_dividend)
        _divisor = abs(_divisor)
        while _dividend > 0:
            if not first:
                countCounter += countCounter
                _divisor += _divisor
            _dividend -= _divisor
            counter += countCounter
            first = False
        if countCounter > 1:
            _dividend += _divisor
            counter -= countCounter

            counter += Solution.divide(self, _dividend, abs(divisor))
        elif countCounter == 1:
            if _dividend < 0:
                counter -= 1
        if negative:
            return counter * -1

        if counter < -2 ** 31:
            return -2 ** 31
        elif counter > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return counter
