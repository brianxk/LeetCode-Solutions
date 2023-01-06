class Solution:
    def reverse(self, x: int) -> int:

        INT_MIN = -2 ** 31
        INT_MAX = (2 ** 31) - 1

        x_reversed = 0

        negative = False

        if x < 0:
            x *= -1
            negative = True

        while x > 0:
            x_reversed *= 10
            x_reversed += x % 10
            x //= 10

        if negative:
            x_reversed *= -1

        if x_reversed > INT_MAX or x_reversed < INT_MIN:
            x_reversed = 0

        return x_reversed
