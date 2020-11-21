class Solution:
    def reverse(self, x: int) -> int:
        y = x
        n = 1
        sign = 1
        result = 0
        if y < 0:
            y *= -1
            sign = -1
        if y < 10:
            return x
        # check place
        while True:
            y = y // 10
            n += 1
            if y < 10:
                break
            else:
                continue
        j = 1
        if x < 0:
            y = x * -1
        else:
            y = x
        for i in reversed(range(n)):
            result += (y // (10 ** i)) * j
            y %= (10 ** i)
            j *= 10
            if result * sign > 2 ** 31 - 1 or result * sign < -2 ** 31:
                return 0
        return result * sign
