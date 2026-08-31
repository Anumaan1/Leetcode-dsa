class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        s = 0

        for digit in str(n):
            if digit != '0':
                x = x * 10 + int(digit)
                s += int(digit)

        return x * s